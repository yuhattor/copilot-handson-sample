import sqlite3
from typing import Optional, Tuple
from contextlib import contextmanager
from dataclasses import dataclass

@dataclass
class User:
	id: int
	display_name: str

class DatabaseConnection:
	def __init__(self, db_path: str = 'database.db'):
		self.db_path = db_path

	@contextmanager
	def get_connection(self):
		conn = sqlite3.connect(self.db_path)
		try:
			yield conn
		finally:
			conn.close()

class UserRepository:
	def __init__(self, db: DatabaseConnection):
		self.db = db

	def get_user_by_id(self, user_id: int) -> Optional[User]:
		query = "SELECT id, display_name FROM users WHERE id = ?"
		params = (user_id,)

		try:
			with self.db.get_connection() as conn:
				cursor = conn.cursor()
				cursor.execute(query, params)
				result = cursor.fetchone()
				
				if result:
					return User(id=result[0], display_name=result[1])
				return None
				
		except sqlite3.Error as e:
			# 実際の環境では適切なログ記録を行うべき
			print(f"Database error occurred: {e}")
			raise

# 使用例
db = DatabaseConnection()
user_repo = UserRepository(db)
user = user_repo.get_user_by_id(1)
