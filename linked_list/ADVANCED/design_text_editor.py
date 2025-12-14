# Design a Text Editor
# Problem: https://leetcode.com/problems/design-a-text-editor/
# Solution:

class TextEditor:
    def __init__(self):
        self.left = []
        self.right = []

    def addText(self, text: str) -> None:
        self.left.extend(text)

    def deleteText(self, k: int) -> int:
        count = min(k, len(self.left))
        for _ in range(count):
            self.left.pop()
        return count

    def cursorLeft(self, k: int) -> str:
        for _ in range(min(k, len(self.left))):
            self.right.append(self.left.pop())
        return ''.join(self.left[-10:])

    def cursorRight(self, k: int) -> str:
        for _ in range(min(k, len(self.right))):
            self.left.append(self.right.pop())
        return ''.join(self.left[-10:])

if __name__ == "__main__":
    # Example use case
    editor = TextEditor()
    editor.addText("leetcode")
    print(editor.deleteText(4))  # 4
    editor.addText("practice")
    print(editor.cursorRight(3))  # "leet"
    print(editor.cursorLeft(8))  # ""
    print(editor.deleteText(10))  # 9
