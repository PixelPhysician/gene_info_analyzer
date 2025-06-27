import unittest
import gzip
import os
from collections import Counter
from utils import parse_gene_info

class TestGeneInfoParsing(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_filename = "test_gene_info.gz"
        content = (
            "#tax_id\tGeneID\tSymbol\tdescription\ttype_of_gene\n"
            "9606\t1\tGENE1\tTest gene 1\tprotein-coding\n"
            "9606\t2\tGENE2\tTest gene 2\tncRNA\n"
            "10090\t3\tGENE3\tMouse gene\tprotein-coding\n"
        )
        with gzip.open(cls.test_filename, 'wt') as f:
            f.write(content)

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.test_filename):
            os.remove(cls.test_filename)

    def test_parse_gene_info_counts(self):
        total, human, types = parse_gene_info(self.test_filename)
        self.assertEqual(total, 3)
        self.assertEqual(human, 2)
        self.assertEqual(Counter(types)['protein-coding'], 2)
        self.assertEqual(Counter(types)['ncRNA'], 1)

    def test_parse_gene_info_type_list(self):
        _, _, types = parse_gene_info(self.test_filename)
        self.assertIn('protein-coding', types)
        self.assertIn('ncRNA', types)

if __name__ == '__main__':
    unittest.main()
