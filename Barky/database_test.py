import unittest
from Barky.database import DatabaseManager



class DatabaseTest(unittest.TestCase):
   
   def test_working(self):
       db = DatabaseManager('bookmarks.db')
       db.create_table('bookmarks_Test', {
            'id': 'integer primary key autoincrement',
            'title': 'text not null',
            'url': 'text not null',
        })
       expected = 3
       ActualRowCount = db.select('bookmarks_Test').fetchall().count()
         
       self.assertEqual(expected,ActualRowCount)