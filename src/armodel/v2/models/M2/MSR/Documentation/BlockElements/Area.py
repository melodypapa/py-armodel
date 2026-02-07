from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class Area(ARObject):
    """
    This element specifies a region in an image map. Image maps enable authors
    to specify regions in an object (e.g. a graphic) and to assign a specific
    activity to each region (e.g. load a document, launch a program etc.). For
    more details refer to the specification of HTML.

    Package: M2::MSR::Documentation::BlockElements::Figure::Area

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 299, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute assigns an access key to an element.
        # An is an individual character (e.
        # g.
        # "B") within the range.
        # If an access key with an to it is pressed, the element comes into activity
                # performed when an element comes is dependent on the element itself.
        self._accesskey: Optional["String"] = None

    @property
    def accesskey(self) -> Optional["String"]:
        """Get accesskey (Pythonic accessor)."""
        return self._accesskey

    @accesskey.setter
    def accesskey(self, value: Optional["String"]) -> None:
        """
        Set accesskey with validation.

        Args:
            value: The accesskey to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._accesskey = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"accesskey must be String or None, got {type(value).__name__}"
            )
        self._accesskey = value
        # This attribute specifies the text to be inserted as an illustrations, shapes
        # or applets, where these displayed by user agents.
        self._alt: Optional["String"] = None

    @property
    def alt(self) -> Optional["String"]:
        """Get alt (Pythonic accessor)."""
        return self._alt

    @alt.setter
    def alt(self, value: Optional["String"]) -> None:
        """
        Set alt with validation.

        Args:
            value: The alt to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._alt = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"alt must be String or None, got {type(value).__name__}"
            )
        self._alt = value
        # Blank separated list of classes.
        self._class: Optional["String"] = None

    @property
    def class(self) -> Optional["String"]:
        """Get class (Pythonic accessor)."""
        return self._class

    @class.setter
    def class(self, value: Optional["String"]) -> None:
        """
        Set class with validation.

        Args:
            value: The class to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._class = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"class must be String or None, got {type(value).__name__}"
            )
        self._class = value
        # This attribute specifies the position and shape on the number of values and
        # their order depend on figure defined.
        self._coords: Optional["String"] = None

    @property
    def coords(self) -> Optional["String"]:
        """Get coords (Pythonic accessor)."""
        return self._coords

    @coords.setter
    def coords(self, value: Optional["String"]) -> None:
        """
        Set coords with validation.

        Args:
            value: The coords to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._coords = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"coords must be String or None, got {type(value).__name__}"
            )
        self._coords = value
        # This attribute specifies the memory location of a web is therefore able to
                # specify a link between the and the target element.
        # 535 Document ID 202: AUTOSAR_FO_TPS_GenericStructureTemplate Template R23-11.
        self._href: Optional["String"] = None

    @property
    def href(self) -> Optional["String"]:
        """Get href (Pythonic accessor)."""
        return self._href

    @href.setter
    def href(self, value: Optional["String"]) -> None:
        """
        Set href with validation.

        Args:
            value: The href to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._href = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"href must be String or None, got {type(value).__name__}"
            )
        self._href = value
        # If this attribute is set, the Area has no associated link.
        self._nohref: Optional["AreaEnumNohref"] = None

    @property
    def nohref(self) -> Optional["AreaEnumNohref"]:
        """Get nohref (Pythonic accessor)."""
        return self._nohref

    @nohref.setter
    def nohref(self, value: Optional["AreaEnumNohref"]) -> None:
        """
        Set nohref with validation.

        Args:
            value: The nohref to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nohref = None
            return

        if not isinstance(value, AreaEnumNohref):
            raise TypeError(
                f"nohref must be AreaEnumNohref or None, got {type(value).__name__}"
            )
        self._nohref = value
        # The ONBLUR-Event occurs, when focus is switched away element.
        # can be stored in this attribute to be performed in.
        self._onblur: Optional["String"] = None

    @property
    def onblur(self) -> Optional["String"]:
        """Get onblur (Pythonic accessor)."""
        return self._onblur

    @onblur.setter
    def onblur(self, value: Optional["String"]) -> None:
        """
        Set onblur with validation.

        Args:
            value: The onblur to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._onblur = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"onblur must be String or None, got {type(value).__name__}"
            )
        self._onblur = value
        # The ONCLICK-Event occurs, if the current element is can be stored in this
        # attribute to be performed in.
        self._onclick: Optional["String"] = None

    @property
    def onclick(self) -> Optional["String"]:
        """Get onclick (Pythonic accessor)."""
        return self._onclick

    @onclick.setter
    def onclick(self, value: Optional["String"]) -> None:
        """
        Set onclick with validation.

        Args:
            value: The onclick to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._onclick = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"onclick must be String or None, got {type(value).__name__}"
            )
        self._onclick = value
        # The ONCLICK-Event occurs, if the current element is can be stored in this
        # attribute to be performed in.
        self._ondblclick: Optional["String"] = None

    @property
    def ondblclick(self) -> Optional["String"]:
        """Get ondblclick (Pythonic accessor)."""
        return self._ondblclick

    @ondblclick.setter
    def ondblclick(self, value: Optional["String"]) -> None:
        """
        Set ondblclick with validation.

        Args:
            value: The ondblclick to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ondblclick = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"ondblclick must be String or None, got {type(value).__name__}"
            )
        self._ondblclick = value
        # The ONFOCUS-Event occurs, if an element comes into through navigation using
                # the tab button).
        # can be stored in this attribute to be performed in.
        self._onfocus: Optional["String"] = None

    @property
    def onfocus(self) -> Optional["String"]:
        """Get onfocus (Pythonic accessor)."""
        return self._onfocus

    @onfocus.setter
    def onfocus(self, value: Optional["String"]) -> None:
        """
        Set onfocus with validation.

        Args:
            value: The onfocus to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._onfocus = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"onfocus must be String or None, got {type(value).__name__}"
            )
        self._onfocus = value
        # The ONKEYDOWN-Event occurs, if a button on the is pressed down.
        # can be stored in this attribute to be performed in.
        self._onkeydown: Optional["String"] = None

    @property
    def onkeydown(self) -> Optional["String"]:
        """Get onkeydown (Pythonic accessor)."""
        return self._onkeydown

    @onkeydown.setter
    def onkeydown(self, value: Optional["String"]) -> None:
        """
        Set onkeydown with validation.

        Args:
            value: The onkeydown to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._onkeydown = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"onkeydown must be String or None, got {type(value).__name__}"
            )
        self._onkeydown = value
        # The ONKEYPRESS-Event occurs, if a button on the is pressed down and released.
        # can be stored in this attribute to be performed in.
        self._onkeypress: Optional["String"] = None

    @property
    def onkeypress(self) -> Optional["String"]:
        """Get onkeypress (Pythonic accessor)."""
        return self._onkeypress

    @onkeypress.setter
    def onkeypress(self, value: Optional["String"]) -> None:
        """
        Set onkeypress with validation.

        Args:
            value: The onkeypress to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._onkeypress = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"onkeypress must be String or None, got {type(value).__name__}"
            )
        self._onkeypress = value
        # The ONKEYUP-Event occurs, if a button on the current released.
        # can be stored in this attribute to be performed in.
        self._onkeyup: Optional["String"] = None

    @property
    def onkeyup(self) -> Optional["String"]:
        """Get onkeyup (Pythonic accessor)."""
        return self._onkeyup

    @onkeyup.setter
    def onkeyup(self, value: Optional["String"]) -> None:
        """
        Set onkeyup with validation.

        Args:
            value: The onkeyup to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._onkeyup = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"onkeyup must be String or None, got {type(value).__name__}"
            )
        self._onkeyup = value
        # The ONMOUSEDOWN-Event occurs, if the mouse button clicking is held down on
                # the current element.
        # can be stored in this attribute to be performed in.
        self._onmousedown: Optional["String"] = None

    @property
    def onmousedown(self) -> Optional["String"]:
        """Get onmousedown (Pythonic accessor)."""
        return self._onmousedown

    @onmousedown.setter
    def onmousedown(self, value: Optional["String"]) -> None:
        """
        Set onmousedown with validation.

        Args:
            value: The onmousedown to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._onmousedown = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"onmousedown must be String or None, got {type(value).__name__}"
            )
        self._onmousedown = value
        # The ONMOUSEMOVE-Event occurs, if the mouse pointer on the current element (i.
        # e.
        # it is located on the can be stored in this attribute to be performed in 535
                # Document ID 202: AUTOSAR_FO_TPS_GenericStructureTemplate Template R23-11.
        self._onmousemove: Optional["String"] = None

    @property
    def onmousemove(self) -> Optional["String"]:
        """Get onmousemove (Pythonic accessor)."""
        return self._onmousemove

    @onmousemove.setter
    def onmousemove(self, value: Optional["String"]) -> None:
        """
        Set onmousemove with validation.

        Args:
            value: The onmousemove to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._onmousemove = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"onmousemove must be String or None, got {type(value).__name__}"
            )
        self._onmousemove = value
        # The ONMOUSEOUT-Event occurs, if the mouse pointer is the current element.
        # can be stored in this attribute to be performed in.
        self._onmouseout: Optional["String"] = None

    @property
    def onmouseout(self) -> Optional["String"]:
        """Get onmouseout (Pythonic accessor)."""
        return self._onmouseout

    @onmouseout.setter
    def onmouseout(self, value: Optional["String"]) -> None:
        """
        Set onmouseout with validation.

        Args:
            value: The onmouseout to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._onmouseout = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"onmouseout must be String or None, got {type(value).__name__}"
            )
        self._onmouseout = value
        # The ONMOUSEOVER-Event occurs, if the mouse pointer to the current element
        # from another location can be stored in this attribute to be performed in.
        self._onmouseover: Optional["String"] = None

    @property
    def onmouseover(self) -> Optional["String"]:
        """Get onmouseover (Pythonic accessor)."""
        return self._onmouseover

    @onmouseover.setter
    def onmouseover(self, value: Optional["String"]) -> None:
        """
        Set onmouseover with validation.

        Args:
            value: The onmouseover to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._onmouseover = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"onmouseover must be String or None, got {type(value).__name__}"
            )
        self._onmouseover = value
        # The ONMOUSEUP-Event occurs if the mouse button clicking is released on the
                # current element.
        # can be stored in this attribute to be performed in.
        self._onmouseup: Optional["String"] = None

    @property
    def onmouseup(self) -> Optional["String"]:
        """Get onmouseup (Pythonic accessor)."""
        return self._onmouseup

    @onmouseup.setter
    def onmouseup(self, value: Optional["String"]) -> None:
        """
        Set onmouseup with validation.

        Args:
            value: The onmouseup to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._onmouseup = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"onmouseup must be String or None, got {type(value).__name__}"
            )
        self._onmouseup = value
        # The shape of the area.
        # Note that in HTML this is RECT.
        self._shape: Optional["AreaEnumShape"] = None

    @property
    def shape(self) -> Optional["AreaEnumShape"]:
        """Get shape (Pythonic accessor)."""
        return self._shape

    @shape.setter
    def shape(self, value: Optional["AreaEnumShape"]) -> None:
        """
        Set shape with validation.

        Args:
            value: The shape to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._shape = None
            return

        if not isinstance(value, AreaEnumShape):
            raise TypeError(
                f"shape must be AreaEnumShape or None, got {type(value).__name__}"
            )
        self._shape = value
        # Information on the associated style.
        self._style: Optional["String"] = None

    @property
    def style(self) -> Optional["String"]:
        """Get style (Pythonic accessor)."""
        return self._style

    @style.setter
    def style(self, value: Optional["String"]) -> None:
        """
        Set style with validation.

        Args:
            value: The style to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._style = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"style must be String or None, got {type(value).__name__}"
            )
        self._style = value
        # This attribute specifies the position of the current element for the
                # corresponding document.
        # shall lie between 0 and 32767.
        # The Tabbing the sequence in which elements are when the user navigates using
                # the keyboard.
        self._tabindex: Optional["String"] = None

    @property
    def tabindex(self) -> Optional["String"]:
        """Get tabindex (Pythonic accessor)."""
        return self._tabindex

    @tabindex.setter
    def tabindex(self, value: Optional["String"]) -> None:
        """
        Set tabindex with validation.

        Args:
            value: The tabindex to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tabindex = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"tabindex must be String or None, got {type(value).__name__}"
            )
        self._tabindex = value
        # Title information of the Area element.
        self._title: Optional["String"] = None

    @property
    def title(self) -> Optional["String"]:
        """Get title (Pythonic accessor)."""
        return self._title

    @title.setter
    def title(self, value: Optional["String"]) -> None:
        """
        Set title with validation.

        Args:
            value: The title to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._title = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"title must be String or None, got {type(value).__name__}"
            )
        self._title = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAccesskey(self) -> "String":
        """
        AUTOSAR-compliant getter for accesskey.

        Returns:
            The accesskey value

        Note:
            Delegates to accesskey property (CODING_RULE_V2_00017)
        """
        return self.accesskey  # Delegates to property

    def setAccesskey(self, value: "String") -> "Area":
        """
        AUTOSAR-compliant setter for accesskey with method chaining.

        Args:
            value: The accesskey to set

        Returns:
            self for method chaining

        Note:
            Delegates to accesskey property setter (gets validation automatically)
        """
        self.accesskey = value  # Delegates to property setter
        return self

    def getAlt(self) -> "String":
        """
        AUTOSAR-compliant getter for alt.

        Returns:
            The alt value

        Note:
            Delegates to alt property (CODING_RULE_V2_00017)
        """
        return self.alt  # Delegates to property

    def setAlt(self, value: "String") -> "Area":
        """
        AUTOSAR-compliant setter for alt with method chaining.

        Args:
            value: The alt to set

        Returns:
            self for method chaining

        Note:
            Delegates to alt property setter (gets validation automatically)
        """
        self.alt = value  # Delegates to property setter
        return self

    def getClass(self) -> "String":
        """
        AUTOSAR-compliant getter for class.

        Returns:
            The class value

        Note:
            Delegates to class property (CODING_RULE_V2_00017)
        """
        return self.class  # Delegates to property

    def setClass(self, value: "String") -> "Area":
        """
        AUTOSAR-compliant setter for class with method chaining.

        Args:
            value: The class to set

        Returns:
            self for method chaining

        Note:
            Delegates to class property setter (gets validation automatically)
        """
        self.class = value  # Delegates to property setter
        return self

    def getCoords(self) -> "String":
        """
        AUTOSAR-compliant getter for coords.

        Returns:
            The coords value

        Note:
            Delegates to coords property (CODING_RULE_V2_00017)
        """
        return self.coords  # Delegates to property

    def setCoords(self, value: "String") -> "Area":
        """
        AUTOSAR-compliant setter for coords with method chaining.

        Args:
            value: The coords to set

        Returns:
            self for method chaining

        Note:
            Delegates to coords property setter (gets validation automatically)
        """
        self.coords = value  # Delegates to property setter
        return self

    def getHref(self) -> "String":
        """
        AUTOSAR-compliant getter for href.

        Returns:
            The href value

        Note:
            Delegates to href property (CODING_RULE_V2_00017)
        """
        return self.href  # Delegates to property

    def setHref(self, value: "String") -> "Area":
        """
        AUTOSAR-compliant setter for href with method chaining.

        Args:
            value: The href to set

        Returns:
            self for method chaining

        Note:
            Delegates to href property setter (gets validation automatically)
        """
        self.href = value  # Delegates to property setter
        return self

    def getNohref(self) -> "AreaEnumNohref":
        """
        AUTOSAR-compliant getter for nohref.

        Returns:
            The nohref value

        Note:
            Delegates to nohref property (CODING_RULE_V2_00017)
        """
        return self.nohref  # Delegates to property

    def setNohref(self, value: "AreaEnumNohref") -> "Area":
        """
        AUTOSAR-compliant setter for nohref with method chaining.

        Args:
            value: The nohref to set

        Returns:
            self for method chaining

        Note:
            Delegates to nohref property setter (gets validation automatically)
        """
        self.nohref = value  # Delegates to property setter
        return self

    def getOnblur(self) -> "String":
        """
        AUTOSAR-compliant getter for onblur.

        Returns:
            The onblur value

        Note:
            Delegates to onblur property (CODING_RULE_V2_00017)
        """
        return self.onblur  # Delegates to property

    def setOnblur(self, value: "String") -> "Area":
        """
        AUTOSAR-compliant setter for onblur with method chaining.

        Args:
            value: The onblur to set

        Returns:
            self for method chaining

        Note:
            Delegates to onblur property setter (gets validation automatically)
        """
        self.onblur = value  # Delegates to property setter
        return self

    def getOnclick(self) -> "String":
        """
        AUTOSAR-compliant getter for onclick.

        Returns:
            The onclick value

        Note:
            Delegates to onclick property (CODING_RULE_V2_00017)
        """
        return self.onclick  # Delegates to property

    def setOnclick(self, value: "String") -> "Area":
        """
        AUTOSAR-compliant setter for onclick with method chaining.

        Args:
            value: The onclick to set

        Returns:
            self for method chaining

        Note:
            Delegates to onclick property setter (gets validation automatically)
        """
        self.onclick = value  # Delegates to property setter
        return self

    def getOndblclick(self) -> "String":
        """
        AUTOSAR-compliant getter for ondblclick.

        Returns:
            The ondblclick value

        Note:
            Delegates to ondblclick property (CODING_RULE_V2_00017)
        """
        return self.ondblclick  # Delegates to property

    def setOndblclick(self, value: "String") -> "Area":
        """
        AUTOSAR-compliant setter for ondblclick with method chaining.

        Args:
            value: The ondblclick to set

        Returns:
            self for method chaining

        Note:
            Delegates to ondblclick property setter (gets validation automatically)
        """
        self.ondblclick = value  # Delegates to property setter
        return self

    def getOnfocus(self) -> "String":
        """
        AUTOSAR-compliant getter for onfocus.

        Returns:
            The onfocus value

        Note:
            Delegates to onfocus property (CODING_RULE_V2_00017)
        """
        return self.onfocus  # Delegates to property

    def setOnfocus(self, value: "String") -> "Area":
        """
        AUTOSAR-compliant setter for onfocus with method chaining.

        Args:
            value: The onfocus to set

        Returns:
            self for method chaining

        Note:
            Delegates to onfocus property setter (gets validation automatically)
        """
        self.onfocus = value  # Delegates to property setter
        return self

    def getOnkeydown(self) -> "String":
        """
        AUTOSAR-compliant getter for onkeydown.

        Returns:
            The onkeydown value

        Note:
            Delegates to onkeydown property (CODING_RULE_V2_00017)
        """
        return self.onkeydown  # Delegates to property

    def setOnkeydown(self, value: "String") -> "Area":
        """
        AUTOSAR-compliant setter for onkeydown with method chaining.

        Args:
            value: The onkeydown to set

        Returns:
            self for method chaining

        Note:
            Delegates to onkeydown property setter (gets validation automatically)
        """
        self.onkeydown = value  # Delegates to property setter
        return self

    def getOnkeypress(self) -> "String":
        """
        AUTOSAR-compliant getter for onkeypress.

        Returns:
            The onkeypress value

        Note:
            Delegates to onkeypress property (CODING_RULE_V2_00017)
        """
        return self.onkeypress  # Delegates to property

    def setOnkeypress(self, value: "String") -> "Area":
        """
        AUTOSAR-compliant setter for onkeypress with method chaining.

        Args:
            value: The onkeypress to set

        Returns:
            self for method chaining

        Note:
            Delegates to onkeypress property setter (gets validation automatically)
        """
        self.onkeypress = value  # Delegates to property setter
        return self

    def getOnkeyup(self) -> "String":
        """
        AUTOSAR-compliant getter for onkeyup.

        Returns:
            The onkeyup value

        Note:
            Delegates to onkeyup property (CODING_RULE_V2_00017)
        """
        return self.onkeyup  # Delegates to property

    def setOnkeyup(self, value: "String") -> "Area":
        """
        AUTOSAR-compliant setter for onkeyup with method chaining.

        Args:
            value: The onkeyup to set

        Returns:
            self for method chaining

        Note:
            Delegates to onkeyup property setter (gets validation automatically)
        """
        self.onkeyup = value  # Delegates to property setter
        return self

    def getOnmousedown(self) -> "String":
        """
        AUTOSAR-compliant getter for onmousedown.

        Returns:
            The onmousedown value

        Note:
            Delegates to onmousedown property (CODING_RULE_V2_00017)
        """
        return self.onmousedown  # Delegates to property

    def setOnmousedown(self, value: "String") -> "Area":
        """
        AUTOSAR-compliant setter for onmousedown with method chaining.

        Args:
            value: The onmousedown to set

        Returns:
            self for method chaining

        Note:
            Delegates to onmousedown property setter (gets validation automatically)
        """
        self.onmousedown = value  # Delegates to property setter
        return self

    def getOnmousemove(self) -> "String":
        """
        AUTOSAR-compliant getter for onmousemove.

        Returns:
            The onmousemove value

        Note:
            Delegates to onmousemove property (CODING_RULE_V2_00017)
        """
        return self.onmousemove  # Delegates to property

    def setOnmousemove(self, value: "String") -> "Area":
        """
        AUTOSAR-compliant setter for onmousemove with method chaining.

        Args:
            value: The onmousemove to set

        Returns:
            self for method chaining

        Note:
            Delegates to onmousemove property setter (gets validation automatically)
        """
        self.onmousemove = value  # Delegates to property setter
        return self

    def getOnmouseout(self) -> "String":
        """
        AUTOSAR-compliant getter for onmouseout.

        Returns:
            The onmouseout value

        Note:
            Delegates to onmouseout property (CODING_RULE_V2_00017)
        """
        return self.onmouseout  # Delegates to property

    def setOnmouseout(self, value: "String") -> "Area":
        """
        AUTOSAR-compliant setter for onmouseout with method chaining.

        Args:
            value: The onmouseout to set

        Returns:
            self for method chaining

        Note:
            Delegates to onmouseout property setter (gets validation automatically)
        """
        self.onmouseout = value  # Delegates to property setter
        return self

    def getOnmouseover(self) -> "String":
        """
        AUTOSAR-compliant getter for onmouseover.

        Returns:
            The onmouseover value

        Note:
            Delegates to onmouseover property (CODING_RULE_V2_00017)
        """
        return self.onmouseover  # Delegates to property

    def setOnmouseover(self, value: "String") -> "Area":
        """
        AUTOSAR-compliant setter for onmouseover with method chaining.

        Args:
            value: The onmouseover to set

        Returns:
            self for method chaining

        Note:
            Delegates to onmouseover property setter (gets validation automatically)
        """
        self.onmouseover = value  # Delegates to property setter
        return self

    def getOnmouseup(self) -> "String":
        """
        AUTOSAR-compliant getter for onmouseup.

        Returns:
            The onmouseup value

        Note:
            Delegates to onmouseup property (CODING_RULE_V2_00017)
        """
        return self.onmouseup  # Delegates to property

    def setOnmouseup(self, value: "String") -> "Area":
        """
        AUTOSAR-compliant setter for onmouseup with method chaining.

        Args:
            value: The onmouseup to set

        Returns:
            self for method chaining

        Note:
            Delegates to onmouseup property setter (gets validation automatically)
        """
        self.onmouseup = value  # Delegates to property setter
        return self

    def getShape(self) -> "AreaEnumShape":
        """
        AUTOSAR-compliant getter for shape.

        Returns:
            The shape value

        Note:
            Delegates to shape property (CODING_RULE_V2_00017)
        """
        return self.shape  # Delegates to property

    def setShape(self, value: "AreaEnumShape") -> "Area":
        """
        AUTOSAR-compliant setter for shape with method chaining.

        Args:
            value: The shape to set

        Returns:
            self for method chaining

        Note:
            Delegates to shape property setter (gets validation automatically)
        """
        self.shape = value  # Delegates to property setter
        return self

    def getStyle(self) -> "String":
        """
        AUTOSAR-compliant getter for style.

        Returns:
            The style value

        Note:
            Delegates to style property (CODING_RULE_V2_00017)
        """
        return self.style  # Delegates to property

    def setStyle(self, value: "String") -> "Area":
        """
        AUTOSAR-compliant setter for style with method chaining.

        Args:
            value: The style to set

        Returns:
            self for method chaining

        Note:
            Delegates to style property setter (gets validation automatically)
        """
        self.style = value  # Delegates to property setter
        return self

    def getTabindex(self) -> "String":
        """
        AUTOSAR-compliant getter for tabindex.

        Returns:
            The tabindex value

        Note:
            Delegates to tabindex property (CODING_RULE_V2_00017)
        """
        return self.tabindex  # Delegates to property

    def setTabindex(self, value: "String") -> "Area":
        """
        AUTOSAR-compliant setter for tabindex with method chaining.

        Args:
            value: The tabindex to set

        Returns:
            self for method chaining

        Note:
            Delegates to tabindex property setter (gets validation automatically)
        """
        self.tabindex = value  # Delegates to property setter
        return self

    def getTitle(self) -> "String":
        """
        AUTOSAR-compliant getter for title.

        Returns:
            The title value

        Note:
            Delegates to title property (CODING_RULE_V2_00017)
        """
        return self.title  # Delegates to property

    def setTitle(self, value: "String") -> "Area":
        """
        AUTOSAR-compliant setter for title with method chaining.

        Args:
            value: The title to set

        Returns:
            self for method chaining

        Note:
            Delegates to title property setter (gets validation automatically)
        """
        self.title = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_accesskey(self, value: Optional["String"]) -> "Area":
        """
        Set accesskey and return self for chaining.

        Args:
            value: The accesskey to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_accesskey("value")
        """
        self.accesskey = value  # Use property setter (gets validation)
        return self

    def with_alt(self, value: Optional["String"]) -> "Area":
        """
        Set alt and return self for chaining.

        Args:
            value: The alt to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_alt("value")
        """
        self.alt = value  # Use property setter (gets validation)
        return self

    def with_class(self, value: Optional["String"]) -> "Area":
        """
        Set class and return self for chaining.

        Args:
            value: The class to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_class("value")
        """
        self.class = value  # Use property setter (gets validation)
        return self

    def with_coords(self, value: Optional["String"]) -> "Area":
        """
        Set coords and return self for chaining.

        Args:
            value: The coords to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_coords("value")
        """
        self.coords = value  # Use property setter (gets validation)
        return self

    def with_href(self, value: Optional["String"]) -> "Area":
        """
        Set href and return self for chaining.

        Args:
            value: The href to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_href("value")
        """
        self.href = value  # Use property setter (gets validation)
        return self

    def with_nohref(self, value: Optional["AreaEnumNohref"]) -> "Area":
        """
        Set nohref and return self for chaining.

        Args:
            value: The nohref to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nohref("value")
        """
        self.nohref = value  # Use property setter (gets validation)
        return self

    def with_onblur(self, value: Optional["String"]) -> "Area":
        """
        Set onblur and return self for chaining.

        Args:
            value: The onblur to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_onblur("value")
        """
        self.onblur = value  # Use property setter (gets validation)
        return self

    def with_onclick(self, value: Optional["String"]) -> "Area":
        """
        Set onclick and return self for chaining.

        Args:
            value: The onclick to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_onclick("value")
        """
        self.onclick = value  # Use property setter (gets validation)
        return self

    def with_ondblclick(self, value: Optional["String"]) -> "Area":
        """
        Set ondblclick and return self for chaining.

        Args:
            value: The ondblclick to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ondblclick("value")
        """
        self.ondblclick = value  # Use property setter (gets validation)
        return self

    def with_onfocus(self, value: Optional["String"]) -> "Area":
        """
        Set onfocus and return self for chaining.

        Args:
            value: The onfocus to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_onfocus("value")
        """
        self.onfocus = value  # Use property setter (gets validation)
        return self

    def with_onkeydown(self, value: Optional["String"]) -> "Area":
        """
        Set onkeydown and return self for chaining.

        Args:
            value: The onkeydown to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_onkeydown("value")
        """
        self.onkeydown = value  # Use property setter (gets validation)
        return self

    def with_onkeypress(self, value: Optional["String"]) -> "Area":
        """
        Set onkeypress and return self for chaining.

        Args:
            value: The onkeypress to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_onkeypress("value")
        """
        self.onkeypress = value  # Use property setter (gets validation)
        return self

    def with_onkeyup(self, value: Optional["String"]) -> "Area":
        """
        Set onkeyup and return self for chaining.

        Args:
            value: The onkeyup to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_onkeyup("value")
        """
        self.onkeyup = value  # Use property setter (gets validation)
        return self

    def with_onmousedown(self, value: Optional["String"]) -> "Area":
        """
        Set onmousedown and return self for chaining.

        Args:
            value: The onmousedown to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_onmousedown("value")
        """
        self.onmousedown = value  # Use property setter (gets validation)
        return self

    def with_onmousemove(self, value: Optional["String"]) -> "Area":
        """
        Set onmousemove and return self for chaining.

        Args:
            value: The onmousemove to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_onmousemove("value")
        """
        self.onmousemove = value  # Use property setter (gets validation)
        return self

    def with_onmouseout(self, value: Optional["String"]) -> "Area":
        """
        Set onmouseout and return self for chaining.

        Args:
            value: The onmouseout to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_onmouseout("value")
        """
        self.onmouseout = value  # Use property setter (gets validation)
        return self

    def with_onmouseover(self, value: Optional["String"]) -> "Area":
        """
        Set onmouseover and return self for chaining.

        Args:
            value: The onmouseover to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_onmouseover("value")
        """
        self.onmouseover = value  # Use property setter (gets validation)
        return self

    def with_onmouseup(self, value: Optional["String"]) -> "Area":
        """
        Set onmouseup and return self for chaining.

        Args:
            value: The onmouseup to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_onmouseup("value")
        """
        self.onmouseup = value  # Use property setter (gets validation)
        return self

    def with_shape(self, value: Optional["AreaEnumShape"]) -> "Area":
        """
        Set shape and return self for chaining.

        Args:
            value: The shape to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_shape("value")
        """
        self.shape = value  # Use property setter (gets validation)
        return self

    def with_style(self, value: Optional["String"]) -> "Area":
        """
        Set style and return self for chaining.

        Args:
            value: The style to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_style("value")
        """
        self.style = value  # Use property setter (gets validation)
        return self

    def with_tabindex(self, value: Optional["String"]) -> "Area":
        """
        Set tabindex and return self for chaining.

        Args:
            value: The tabindex to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tabindex("value")
        """
        self.tabindex = value  # Use property setter (gets validation)
        return self

    def with_title(self, value: Optional["String"]) -> "Area":
        """
        Set title and return self for chaining.

        Args:
            value: The title to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_title("value")
        """
        self.title = value  # Use property setter (gets validation)
        return self
