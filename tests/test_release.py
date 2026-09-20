import importlib.util, pathlib, tempfile, unittest, zipfile
ROOT=pathlib.Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('build',ROOT/'scripts/build.py')
b=importlib.util.module_from_spec(spec);spec.loader.exec_module(b)
class ReleaseTests(unittest.TestCase):
    def test_inventory_and_runtime(self):
        files=b.make_files(ROOT);b.verify_files(files)
        self.assertEqual(len(files),7)
        self.assertEqual({p for p in files if p.startswith('Addon/')},{'Addon/'+b.ARCHIVE,'Addon/'+b.ARCHIVE+'.stream','Addon/'+b.ARCHIVE+'.gpu_resources'})
    def test_tamper_detection(self):
        files=b.make_files(ROOT);files['thumbnail.png']+=b'x'
        with self.assertRaises(ValueError):b.verify_files(files)
    def test_missing_file_detection(self):
        files=b.make_files(ROOT);del files['thumbnail.png']
        with self.assertRaises(ValueError):b.verify_files(files)
    def test_repeatable_zip(self):
        with tempfile.TemporaryDirectory() as folder:
            a=b.build(pathlib.Path(folder)/'a',ROOT);c=b.build(pathlib.Path(folder)/'b',ROOT)
            self.assertEqual(a.read_bytes(),c.read_bytes())
            with zipfile.ZipFile(a) as z:self.assertIsNone(z.testzip())
if __name__=='__main__':unittest.main()
