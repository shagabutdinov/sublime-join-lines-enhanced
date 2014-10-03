import unittest

try: # suppress import exception when loading package to sublime
  from join_lines import join
except ImportError:
  pass

class JoinStringTest(unittest.TestCase):

  def test_join_without_new_line_is_text(self):
    self.assertEqual('NONE', join('NONE'))

  def test_join_is_joined_string(self):
    self.assertEqual('ONE TWO', join('ONE\nTWO'))

  def test_join_is_joined_string_without_spaces(self):
    self.assertEqual('ONE TWO', join('ONE\n  TWO'))

  def test_join_is_joined_with_spaces(self):
    self.assertEqual('ONE TWO', join('ONE  \n  TWO'))

  def test_join_is_joined_with_prepending_dot(self):
    self.assertEqual('ONE.TWO', join('ONE\n .TWO'))

  def test_join_is_joined_with_prepending_closing_bracket(self):
    self.assertEqual('ONE) TWO', join('ONE\n) TWO'))

  def test_join_is_joined_with_prepending_closing_bracket_2(self):
    self.assertEqual('ONE] TWO', join('ONE\n] TWO'))

  def test_join_is_joined_with_prepending_closing_bracket_3(self):
    self.assertEqual('ONE} TWO', join('ONE\n} TWO'))

  def test_join_is_joined_with_prepending_closing_quote(self):
    self.assertEqual('ONE"', join('ONE\n "'))

  def test_join_is_joined_with_prepending_double_colon(self):
    self.assertEqual('ONE::TWO', join('ONE::\n TWO'))

  def test_join_is_joined_with_appending_dot(self):
    self.assertEqual('ONE.TWO', join('ONE.\n TWO'))

  def test_join_is_joined_with_appending_bracket(self):
    self.assertEqual('ONE(TWO', join('ONE(\n TWO'))

  def test_join_is_joined_with_appending_bracket_2(self):
    self.assertEqual('ONE[TWO', join('ONE[\n TWO'))

  def test_join_is_joined_with_appending_bracket_3(self):
    self.assertEqual('ONE{TWO', join('ONE{\n TWO'))

  def test_join_is_joined_with_appending_quote(self):
    self.assertEqual('ONE"TWO', join('ONE"\n TWO'))

  def test_join_is_joined_with_following_minus_greater(self):
    self.assertEqual('ONE->TWO', join('ONE\n ->TWO'))

  def test_join_is_joined_with_following_double_colon(self):
    self.assertEqual('ONE::TWO', join('ONE\n ::TWO'))

  def test_join_is_joined_with_preceding_minus_greater(self):
    self.assertEqual('ONE->TWO', join('ONE->\n TWO'))

if __name__ == '__main__':
  unittest.main()