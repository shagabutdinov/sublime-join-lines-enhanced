import sublime
import sublime_plugin
import re
from JoinLinesEnhanced import join_lines

class JoinLinesEnhanced(sublime_plugin.TextCommand):
  def run(self, edit):
    selections = []
    for sel in self.view.sel():
      start, end = self._join(edit, sel.a, sel.b)
      selections.append(sublime.Region(start, end))

    self.view.sel().clear()
    self.view.sel().add_all(selections)

  def _join(self, edit, start, end):
    cursor = [start, end]
    selection = True

    if start == end:
      is_new_line = self.view.substr(sublime.Region(start, start - 1)) != "\n"
      if start > 0 and is_new_line:
        start -= 1

      selection = False
      text = self.view.substr(sublime.Region(start, self.view.size()))
      matches = re.search(r'([^\n]*\n[^\n]*)(\n|$)', text)
      if matches == None:
        return cursor

      end = matches.end(1)
      end += start
    else:
      if start > end:
        start, end = end, start

    text = self.view.substr(sublime.Region(start, end))
    cursor = start + re.search("\n", text).start(0)
    text = join_lines.join(text)

    self.view.replace(edit, sublime.Region(start, end), text)

    if selection:
      cursor = [start, start + len(text)]
    else:
      if self.view.substr(sublime.Region(cursor, cursor + 1)) == ' ':
        cursor += 1
      cursor = [cursor] * 2

    return cursor