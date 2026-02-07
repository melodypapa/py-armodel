from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class Map(ARObject):
    """
    Image maps enable authors to specify regions of an image or object and
    assign a specific action to each region (e.g., retrieve a document, run a
    program, etc.) When the region is activated by the user, the action is
    executed. The class follows the html approach and is intended to support
    interactive documents.
    
    Package: M2::MSR::Documentation::BlockElements::Figure::Map
    
    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 305, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # authors to specify regions in an object (e.
        # g.
        # and to assign a specific activity to each region a document, launch a program
                # etc.
        # ).
        self._area: "Area" = None

    @property
    def area(self) -> "Area":
        """Get area (Pythonic accessor)."""
        return self._area

    @area.setter
    def area(self, value: "Area") -> None:
        """
        Set area with validation.
        
        Args:
            value: The area to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, Area):
            raise TypeError(
                f"area must be Area, got {type(value).__name__}"
            )
        self._area = value
        # This attribute assigns a class name or set of class names element.
        # Any number of elements may be assigned class name or set of class names.
        # Multiple shall be separated by white space names are typically used to apply
                # CSS to an element.
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
        # This attribute assigns a name to the image map in the This name can be used
                # to be referenced in image through the attribute USEMAP.
        # Although not actually necessary in the MSR model, it was order to support the
                # MAPs which were created.
        self._name: Optional["NameToken"] = None

    @property
    def name(self) -> Optional["NameToken"]:
        """Get name (Pythonic accessor)."""
        return self._name

    @name.setter
    def name(self, value: Optional["NameToken"]) -> None:
        """
        Set name with validation.
        
        Args:
            value: The name to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._name = None
            return

        if not isinstance(value, NameToken):
            raise TypeError(
                f"name must be NameToken or None, got {type(value).__name__}"
            )
        self._name = value
        # The ONCLICK-Event occurs, if the current element is A script can be stored in
        # this attribute to be the Event.
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
        # The ONDBLCLICK-Event occurs, if the current Event is A script can be stored
                # in this attribute performed in the Event.
        # 535 Document ID 202: AUTOSAR_FO_TPS_GenericStructureTemplate Template R23-11.
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
        # it is located on the can be stored in this attribute to be performed in.
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
        # This attribute offers advisory information.
        # Some Web display this information as tooltips.
        # may make this information available to additional information about the
                # element.
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

    def getArea(self) -> "Area":
        """
        AUTOSAR-compliant getter for area.
        
        Returns:
            The area value
        
        Note:
            Delegates to area property (CODING_RULE_V2_00017)
        """
        return self.area  # Delegates to property

    def setArea(self, value: "Area") -> "Map":
        """
        AUTOSAR-compliant setter for area with method chaining.
        
        Args:
            value: The area to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to area property setter (gets validation automatically)
        """
        self.area = value  # Delegates to property setter
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

    def setClass(self, value: "String") -> "Map":
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

    def getName(self) -> "NameToken":
        """
        AUTOSAR-compliant getter for name.
        
        Returns:
            The name value
        
        Note:
            Delegates to name property (CODING_RULE_V2_00017)
        """
        return self.name  # Delegates to property

    def setName(self, value: "NameToken") -> "Map":
        """
        AUTOSAR-compliant setter for name with method chaining.
        
        Args:
            value: The name to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to name property setter (gets validation automatically)
        """
        self.name = value  # Delegates to property setter
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

    def setOnclick(self, value: "String") -> "Map":
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

    def setOndblclick(self, value: "String") -> "Map":
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

    def getOnkeydown(self) -> "String":
        """
        AUTOSAR-compliant getter for onkeydown.
        
        Returns:
            The onkeydown value
        
        Note:
            Delegates to onkeydown property (CODING_RULE_V2_00017)
        """
        return self.onkeydown  # Delegates to property

    def setOnkeydown(self, value: "String") -> "Map":
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

    def setOnkeypress(self, value: "String") -> "Map":
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

    def setOnkeyup(self, value: "String") -> "Map":
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

    def setOnmousedown(self, value: "String") -> "Map":
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

    def setOnmousemove(self, value: "String") -> "Map":
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

    def setOnmouseout(self, value: "String") -> "Map":
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

    def setOnmouseover(self, value: "String") -> "Map":
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

    def setOnmouseup(self, value: "String") -> "Map":
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

    def getTitle(self) -> "String":
        """
        AUTOSAR-compliant getter for title.
        
        Returns:
            The title value
        
        Note:
            Delegates to title property (CODING_RULE_V2_00017)
        """
        return self.title  # Delegates to property

    def setTitle(self, value: "String") -> "Map":
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

    def with_area(self, value: "Area") -> "Map":
        """
        Set area and return self for chaining.
        
        Args:
            value: The area to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_area("value")
        """
        self.area = value  # Use property setter (gets validation)
        return self

    def with_class(self, value: Optional["String"]) -> "Map":
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

    def with_name(self, value: Optional["NameToken"]) -> "Map":
        """
        Set name and return self for chaining.
        
        Args:
            value: The name to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_name("value")
        """
        self.name = value  # Use property setter (gets validation)
        return self

    def with_onclick(self, value: Optional["String"]) -> "Map":
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

    def with_ondblclick(self, value: Optional["String"]) -> "Map":
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

    def with_onkeydown(self, value: Optional["String"]) -> "Map":
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

    def with_onkeypress(self, value: Optional["String"]) -> "Map":
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

    def with_onkeyup(self, value: Optional["String"]) -> "Map":
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

    def with_onmousedown(self, value: Optional["String"]) -> "Map":
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

    def with_onmousemove(self, value: Optional["String"]) -> "Map":
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

    def with_onmouseout(self, value: Optional["String"]) -> "Map":
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

    def with_onmouseover(self, value: Optional["String"]) -> "Map":
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

    def with_onmouseup(self, value: Optional["String"]) -> "Map":
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

    def with_title(self, value: Optional["String"]) -> "Map":
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