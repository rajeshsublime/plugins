import sublime, sublimeplugin
  
class CustomStatusBar(sublimeplugin.Plugin):
    def onModified(self, view):
        totalLines = len(view.lines(sublime.Region(0L, view.size())))
        msg = '%d lines' % (totalLines)
        sublime.setStatus('totalLines', msg)

    def onLoaded(self, view):
        self.onModified(view)
