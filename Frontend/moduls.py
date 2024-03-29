from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Color, RoundedRectangle


class RoundedButton(Button):
    """
    RoundedButton:
        Class inherited from `Button`,
        which represents a rounded button with custom background color and behavior.
    """

    def __init__(self, **kwargs):
        super(RoundedButton, self).__init__(**kwargs)
        self.background_color = (0, 0, 0, 0)
        self.background_normal = ""
        with self.canvas.before:
            Color(0.0, 0.84, 0.64, 1)
            self.rect = RoundedRectangle(
                size=self.size,
                pos=self.pos,
                radius=[8],
            )
        self.bind(
            pos=self.update_rect,
            size=self.update_rect,
        )

    def update_rect(self, *args):
        """
        update_rect:
            Updates the position and size of the rounded rectangle shape
            based on the position and size of the button.
        """
        self.rect.pos = self.pos
        self.rect.size = self.size

    def on_press(self):
        """
        on_press:
            Event handler for the button's press event.
            Updates the button's background color when pressed.
        """
        self.background_color = (0.0, 0.84, 0.64, 0.4)
        self.background_normal = ""

    def on_release(self):
        """
        on_release:
            Event handler for the button's release event.
            Resets the button's background color when released.
        """
        self.background_color = (0, 0, 0, 0)
        self.background_normal = ""


class DarkenedGridLayout(GridLayout):
    """
    DarkenedGridLayout:
        Class inherited from `GridLayout`,
        which represents a grid layout with a darkened background.
    """

    def __init__(self, **kwargs):
        super(DarkenedGridLayout, self).__init__(**kwargs)
        with self.canvas.before:
            Color(0, 0, 0, 0.5)
            self.rect = RoundedRectangle(
                size=self.size,
                pos=self.pos,
            )
        self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, *args):
        """
        update_rect:
            Updates the position and size of the rounded rectangle shape
            based on the position and size of the grid layout.
        """
        self.rect.pos = self.pos
        self.rect.size = self.size


class CustomLabel(Label):
    """
    CustomLabel:
        Class inherited from `Label`,
        which represents a custom label with specific text properties.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text_size = (self.width + 30, self.height - 10)
        self.halign = "left"
        self.valign = "center"
