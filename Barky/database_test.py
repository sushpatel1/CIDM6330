from database import DatabaseManager
import unittest


class DatabaseTest(unittest.TestCase):
   
   def test_working(self):
       db = DatabaseManager('bookmarks.db')
       db.create_table('bookmarks_Test', {
            'id': 'integer primary key autoincrement',
            'title': 'text not null',
            'url': 'text not null',
        })
        
       ActualRowCount = db.select('bookmarks_Test').fetchall().count()
       self.assertEqual(3,ActualRowCount)

      