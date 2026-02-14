"""
AUTOSAR Package - Figure

Package: M2::MSR::Documentation::BlockElements::Figure
"""


from __future__ import annotations

from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.EngineeringObject import (
    EngineeringObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
    NameToken,
    String,
)
from armodel.v2.models.M2.MSR.Documentation.BlockElements.PaginationAndView import (
    Paginateable,
)
from armodel.v2.models.M2.MSR.Documentation.TextModel.LanguageDataModel import (
    LanguageSpecific,
    PgwideEnum,
)


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
        self._accesskey: Optional[String] = None

    @property
    def accesskey(self) -> Optional[String]:
        """Get accesskey (Pythonic accessor)."""
        return self._accesskey

    @accesskey.setter
    def accesskey(self, value: Optional[String]) -> None:
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

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"accesskey must be String or str or None, got {type(value).__name__}"
            )
        self._accesskey = value
        # or applets, where these displayed by user agents.
        self._alt: Optional[String] = None

    @property
    def alt(self) -> Optional[String]:
        """Get alt (Pythonic accessor)."""
        return self._alt

    @alt.setter
    def alt(self, value: Optional[String]) -> None:
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

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"alt must be String or str or None, got {type(value).__name__}"
            )
        self._alt = value
        self._class_name: Optional[String] = None

    @property
    def class_name(self) -> Optional[String]:
        """Get class_name (Pythonic accessor)."""
        return self._class_name

    @class_name.setter
    def class_name(self, value: Optional[String]) -> None:
        """
        Set class_name with validation.
        
        Args:
            value: The class_name to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._class_name = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"class_name must be String or str or None, got {type(value).__name__}"
            )
        self._class_name = value
        # their order depend on figure defined.
        self._coords: Optional[String] = None

    @property
    def coords(self) -> Optional[String]:
        """Get coords (Pythonic accessor)."""
        return self._coords

    @coords.setter
    def coords(self, value: Optional[String]) -> None:
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

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"coords must be String or str or None, got {type(value).__name__}"
            )
        self._coords = value
                # specify a link between the and the target element.
        # 535 Document ID 202: AUTOSAR_FO_TPS_GenericStructureTemplate Template R23-11.
        self._href: Optional[String] = None

    @property
    def href(self) -> Optional[String]:
        """Get href (Pythonic accessor)."""
        return self._href

    @href.setter
    def href(self, value: Optional[String]) -> None:
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

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"href must be String or str or None, got {type(value).__name__}"
            )
        self._href = value
        self._nohref: Optional[AreaEnumNohref] = None

    @property
    def nohref(self) -> Optional[AreaEnumNohref]:
        """Get nohref (Pythonic accessor)."""
        return self._nohref

    @nohref.setter
    def nohref(self, value: Optional[AreaEnumNohref]) -> None:
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
        # can be stored in this attribute to be performed in.
        self._onblur: Optional[String] = None

    @property
    def onblur(self) -> Optional[String]:
        """Get onblur (Pythonic accessor)."""
        return self._onblur

    @onblur.setter
    def onblur(self, value: Optional[String]) -> None:
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

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"onblur must be String or str or None, got {type(value).__name__}"
            )
        self._onblur = value
        # attribute to be performed in.
        self._onclick: Optional[String] = None

    @property
    def onclick(self) -> Optional[String]:
        """Get onclick (Pythonic accessor)."""
        return self._onclick

    @onclick.setter
    def onclick(self, value: Optional[String]) -> None:
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

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"onclick must be String or str or None, got {type(value).__name__}"
            )
        self._onclick = value
        # attribute to be performed in.
        self._ondblclick: Optional[String] = None

    @property
    def ondblclick(self) -> Optional[String]:
        """Get ondblclick (Pythonic accessor)."""
        return self._ondblclick

    @ondblclick.setter
    def ondblclick(self, value: Optional[String]) -> None:
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

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"ondblclick must be String or str or None, got {type(value).__name__}"
            )
        self._ondblclick = value
                # the tab button).
        # can be stored in this attribute to be performed in.
        self._onfocus: Optional[String] = None

    @property
    def onfocus(self) -> Optional[String]:
        """Get onfocus (Pythonic accessor)."""
        return self._onfocus

    @onfocus.setter
    def onfocus(self, value: Optional[String]) -> None:
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

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"onfocus must be String or str or None, got {type(value).__name__}"
            )
        self._onfocus = value
        # can be stored in this attribute to be performed in.
        self._onkeydown: Optional[String] = None

    @property
    def onkeydown(self) -> Optional[String]:
        """Get onkeydown (Pythonic accessor)."""
        return self._onkeydown

    @onkeydown.setter
    def onkeydown(self, value: Optional[String]) -> None:
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

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"onkeydown must be String or str or None, got {type(value).__name__}"
            )
        self._onkeydown = value
        # can be stored in this attribute to be performed in.
        self._onkeypress: Optional[String] = None

    @property
    def onkeypress(self) -> Optional[String]:
        """Get onkeypress (Pythonic accessor)."""
        return self._onkeypress

    @onkeypress.setter
    def onkeypress(self, value: Optional[String]) -> None:
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

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"onkeypress must be String or str or None, got {type(value).__name__}"
            )
        self._onkeypress = value
        # can be stored in this attribute to be performed in.
        self._onkeyup: Optional[String] = None

    @property
    def onkeyup(self) -> Optional[String]:
        """Get onkeyup (Pythonic accessor)."""
        return self._onkeyup

    @onkeyup.setter
    def onkeyup(self, value: Optional[String]) -> None:
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

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"onkeyup must be String or str or None, got {type(value).__name__}"
            )
        self._onkeyup = value
                # the current element.
        # can be stored in this attribute to be performed in.
        self._onmousedown: Optional[String] = None

    @property
    def onmousedown(self) -> Optional[String]:
        """Get onmousedown (Pythonic accessor)."""
        return self._onmousedown

    @onmousedown.setter
    def onmousedown(self, value: Optional[String]) -> None:
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

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"onmousedown must be String or str or None, got {type(value).__name__}"
            )
        self._onmousedown = value
        # e.
        # it is located on the can be stored in this attribute to be performed in 535
                # Document ID 202: AUTOSAR_FO_TPS_GenericStructureTemplate Template R23-11.
        self._onmousemove: Optional[String] = None

    @property
    def onmousemove(self) -> Optional[String]:
        """Get onmousemove (Pythonic accessor)."""
        return self._onmousemove

    @onmousemove.setter
    def onmousemove(self, value: Optional[String]) -> None:
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

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"onmousemove must be String or str or None, got {type(value).__name__}"
            )
        self._onmousemove = value
        # can be stored in this attribute to be performed in.
        self._onmouseout: Optional[String] = None

    @property
    def onmouseout(self) -> Optional[String]:
        """Get onmouseout (Pythonic accessor)."""
        return self._onmouseout

    @onmouseout.setter
    def onmouseout(self, value: Optional[String]) -> None:
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

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"onmouseout must be String or str or None, got {type(value).__name__}"
            )
        self._onmouseout = value
        # from another location can be stored in this attribute to be performed in.
        self._onmouseover: Optional[String] = None

    @property
    def onmouseover(self) -> Optional[String]:
        """Get onmouseover (Pythonic accessor)."""
        return self._onmouseover

    @onmouseover.setter
    def onmouseover(self, value: Optional[String]) -> None:
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

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"onmouseover must be String or str or None, got {type(value).__name__}"
            )
        self._onmouseover = value
                # current element.
        # can be stored in this attribute to be performed in.
        self._onmouseup: Optional[String] = None

    @property
    def onmouseup(self) -> Optional[String]:
        """Get onmouseup (Pythonic accessor)."""
        return self._onmouseup

    @onmouseup.setter
    def onmouseup(self, value: Optional[String]) -> None:
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

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"onmouseup must be String or str or None, got {type(value).__name__}"
            )
        self._onmouseup = value
        # Note that in HTML this is RECT.
        self._shape: Optional[AreaEnumShape] = None

    @property
    def shape(self) -> Optional[AreaEnumShape]:
        """Get shape (Pythonic accessor)."""
        return self._shape

    @shape.setter
    def shape(self, value: Optional[AreaEnumShape]) -> None:
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
        self._style: Optional[String] = None

    @property
    def style(self) -> Optional[String]:
        """Get style (Pythonic accessor)."""
        return self._style

    @style.setter
    def style(self, value: Optional[String]) -> None:
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

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"style must be String or str or None, got {type(value).__name__}"
            )
        self._style = value
                # corresponding document.
        # shall lie between 0 and 32767.
        # The Tabbing the sequence in which elements are when the user navigates using
                # the keyboard.
        self._tabindex: Optional[String] = None

    @property
    def tabindex(self) -> Optional[String]:
        """Get tabindex (Pythonic accessor)."""
        return self._tabindex

    @tabindex.setter
    def tabindex(self, value: Optional[String]) -> None:
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

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"tabindex must be String or str or None, got {type(value).__name__}"
            )
        self._tabindex = value
        self._title: Optional[String] = None

    @property
    def title(self) -> Optional[String]:
        """Get title (Pythonic accessor)."""
        return self._title

    @title.setter
    def title(self, value: Optional[String]) -> None:
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

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"title must be String or str or None, got {type(value).__name__}"
            )
        self._title = value

    def with_l_graphic(self, value):
        """
        Set l_graphic and return self for chaining.

        Args:
            value: The l_graphic to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_l_graphic("value")
        """
        self.l_graphic = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAccesskey(self) -> String:
        """
        AUTOSAR-compliant getter for accesskey.
        
        Returns:
            The accesskey value
        
        Note:
            Delegates to accesskey property (CODING_RULE_V2_00017)
        """
        return self.accesskey  # Delegates to property

    def setAccesskey(self, value: String) -> Area:
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

    def getAlt(self) -> String:
        """
        AUTOSAR-compliant getter for alt.
        
        Returns:
            The alt value
        
        Note:
            Delegates to alt property (CODING_RULE_V2_00017)
        """
        return self.alt  # Delegates to property

    def setAlt(self, value: String) -> Area:
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

    def getClass(self) -> String:
        """
        AUTOSAR-compliant getter for class.
        
        Returns:
            The class value
        
        Note:
            Delegates to class_name property (CODING_RULE_V2_00017)
        """
        return self.class_name  # Delegates to property

    def setClass(self, value: String) -> Area:
        """
        AUTOSAR-compliant setter for class_name with method chaining.

        Args:
            value: The class_name to set

        Returns:
            self for method chaining

        Note:
            Delegates to class_name property setter (gets validation automatically)
        """
        self.class_name = value  # Delegates to property setter
        return self

    def getCoords(self) -> String:
        """
        AUTOSAR-compliant getter for coords.
        
        Returns:
            The coords value
        
        Note:
            Delegates to coords property (CODING_RULE_V2_00017)
        """
        return self.coords  # Delegates to property

    def setCoords(self, value: String) -> Area:
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

    def getHref(self) -> String:
        """
        AUTOSAR-compliant getter for href.
        
        Returns:
            The href value
        
        Note:
            Delegates to href property (CODING_RULE_V2_00017)
        """
        return self.href  # Delegates to property

    def setHref(self, value: String) -> Area:
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

    def getNohref(self) -> AreaEnumNohref:
        """
        AUTOSAR-compliant getter for nohref.
        
        Returns:
            The nohref value
        
        Note:
            Delegates to nohref property (CODING_RULE_V2_00017)
        """
        return self.nohref  # Delegates to property

    def setNohref(self, value: AreaEnumNohref) -> Area:
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

    def getOnblur(self) -> String:
        """
        AUTOSAR-compliant getter for onblur.
        
        Returns:
            The onblur value
        
        Note:
            Delegates to onblur property (CODING_RULE_V2_00017)
        """
        return self.onblur  # Delegates to property

    def setOnblur(self, value: String) -> Area:
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

    def getOnclick(self) -> String:
        """
        AUTOSAR-compliant getter for onclick.
        
        Returns:
            The onclick value
        
        Note:
            Delegates to onclick property (CODING_RULE_V2_00017)
        """
        return self.onclick  # Delegates to property

    def setOnclick(self, value: String) -> Area:
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

    def getOndblclick(self) -> String:
        """
        AUTOSAR-compliant getter for ondblclick.
        
        Returns:
            The ondblclick value
        
        Note:
            Delegates to ondblclick property (CODING_RULE_V2_00017)
        """
        return self.ondblclick  # Delegates to property

    def setOndblclick(self, value: String) -> Area:
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

    def getOnfocus(self) -> String:
        """
        AUTOSAR-compliant getter for onfocus.
        
        Returns:
            The onfocus value
        
        Note:
            Delegates to onfocus property (CODING_RULE_V2_00017)
        """
        return self.onfocus  # Delegates to property

    def setOnfocus(self, value: String) -> Area:
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

    def getOnkeydown(self) -> String:
        """
        AUTOSAR-compliant getter for onkeydown.
        
        Returns:
            The onkeydown value
        
        Note:
            Delegates to onkeydown property (CODING_RULE_V2_00017)
        """
        return self.onkeydown  # Delegates to property

    def setOnkeydown(self, value: String) -> Area:
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

    def getOnkeypress(self) -> String:
        """
        AUTOSAR-compliant getter for onkeypress.
        
        Returns:
            The onkeypress value
        
        Note:
            Delegates to onkeypress property (CODING_RULE_V2_00017)
        """
        return self.onkeypress  # Delegates to property

    def setOnkeypress(self, value: String) -> Area:
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

    def getOnkeyup(self) -> String:
        """
        AUTOSAR-compliant getter for onkeyup.
        
        Returns:
            The onkeyup value
        
        Note:
            Delegates to onkeyup property (CODING_RULE_V2_00017)
        """
        return self.onkeyup  # Delegates to property

    def setOnkeyup(self, value: String) -> Area:
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

    def getOnmousedown(self) -> String:
        """
        AUTOSAR-compliant getter for onmousedown.
        
        Returns:
            The onmousedown value
        
        Note:
            Delegates to onmousedown property (CODING_RULE_V2_00017)
        """
        return self.onmousedown  # Delegates to property

    def setOnmousedown(self, value: String) -> Area:
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

    def getOnmousemove(self) -> String:
        """
        AUTOSAR-compliant getter for onmousemove.
        
        Returns:
            The onmousemove value
        
        Note:
            Delegates to onmousemove property (CODING_RULE_V2_00017)
        """
        return self.onmousemove  # Delegates to property

    def setOnmousemove(self, value: String) -> Area:
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

    def getOnmouseout(self) -> String:
        """
        AUTOSAR-compliant getter for onmouseout.
        
        Returns:
            The onmouseout value
        
        Note:
            Delegates to onmouseout property (CODING_RULE_V2_00017)
        """
        return self.onmouseout  # Delegates to property

    def setOnmouseout(self, value: String) -> Area:
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

    def getOnmouseover(self) -> String:
        """
        AUTOSAR-compliant getter for onmouseover.
        
        Returns:
            The onmouseover value
        
        Note:
            Delegates to onmouseover property (CODING_RULE_V2_00017)
        """
        return self.onmouseover  # Delegates to property

    def setOnmouseover(self, value: String) -> Area:
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

    def getOnmouseup(self) -> String:
        """
        AUTOSAR-compliant getter for onmouseup.
        
        Returns:
            The onmouseup value
        
        Note:
            Delegates to onmouseup property (CODING_RULE_V2_00017)
        """
        return self.onmouseup  # Delegates to property

    def setOnmouseup(self, value: String) -> Area:
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

    def getShape(self) -> AreaEnumShape:
        """
        AUTOSAR-compliant getter for shape.
        
        Returns:
            The shape value
        
        Note:
            Delegates to shape property (CODING_RULE_V2_00017)
        """
        return self.shape  # Delegates to property

    def setShape(self, value: AreaEnumShape) -> Area:
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

    def getStyle(self) -> String:
        """
        AUTOSAR-compliant getter for style.
        
        Returns:
            The style value
        
        Note:
            Delegates to style property (CODING_RULE_V2_00017)
        """
        return self.style  # Delegates to property

    def setStyle(self, value: String) -> Area:
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

    def getTabindex(self) -> String:
        """
        AUTOSAR-compliant getter for tabindex.
        
        Returns:
            The tabindex value
        
        Note:
            Delegates to tabindex property (CODING_RULE_V2_00017)
        """
        return self.tabindex  # Delegates to property

    def setTabindex(self, value: String) -> Area:
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

    def getTitle(self) -> String:
        """
        AUTOSAR-compliant getter for title.
        
        Returns:
            The title value
        
        Note:
            Delegates to title property (CODING_RULE_V2_00017)
        """
        return self.title  # Delegates to property

    def setTitle(self, value: String) -> Area:
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

    def with_accesskey(self, value: Optional[String]) -> Area:
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

    def with_alt(self, value: Optional[String]) -> Area:
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

    def with_class_name(self, value: Optional[String]) -> Area:
        """
        Set class_name and return self for chaining.
        
        Args:
            value: The class_name to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_class_name("value")
        """
        self.class_name = value  # Use property setter (gets validation)
        return self

    def with_coords(self, value: Optional[String]) -> Area:
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

    def with_href(self, value: Optional[String]) -> Area:
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

    def with_nohref(self, value: Optional[AreaEnumNohref]) -> Area:
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

    def with_onblur(self, value: Optional[String]) -> Area:
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

    def with_onclick(self, value: Optional[String]) -> Area:
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

    def with_ondblclick(self, value: Optional[String]) -> Area:
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

    def with_onfocus(self, value: Optional[String]) -> Area:
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

    def with_onkeydown(self, value: Optional[String]) -> Area:
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

    def with_onkeypress(self, value: Optional[String]) -> Area:
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

    def with_onkeyup(self, value: Optional[String]) -> Area:
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

    def with_onmousedown(self, value: Optional[String]) -> Area:
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

    def with_onmousemove(self, value: Optional[String]) -> Area:
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

    def with_onmouseout(self, value: Optional[String]) -> Area:
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

    def with_onmouseover(self, value: Optional[String]) -> Area:
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

    def with_onmouseup(self, value: Optional[String]) -> Area:
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

    def with_shape(self, value: Optional[AreaEnumShape]) -> Area:
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

    def with_style(self, value: Optional[String]) -> Area:
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

    def with_tabindex(self, value: Optional[String]) -> Area:
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

    def with_title(self, value: Optional[String]) -> Area:
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



class Graphic(EngineeringObject):
    """
    This class represents an artifact containing the image to be inserted in the
    document
    
    Package: M2::MSR::Documentation::BlockElements::Figure::Graphic
    
    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 302, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies how the graphic shall be displayed in an editor.
        # attribute is missing,.
        self._editfit: Optional[GraphicFitEnum] = None

    @property
    def editfit(self) -> Optional[GraphicFitEnum]:
        """Get editfit (Pythonic accessor)."""
        return self._editfit

    @editfit.setter
    def editfit(self, value: Optional[GraphicFitEnum]) -> None:
        """
        Set editfit with validation.
        
        Args:
            value: The editfit to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._editfit = None
            return

        if not isinstance(value, GraphicFitEnum):
            raise TypeError(
                f"editfit must be GraphicFitEnum or None, got {type(value).__name__}"
            )
        self._editfit = value
                # added to the number in the units are: cm, mm, px, pt.
        # The default unit.
        self._editHeight: Optional[String] = None

    @property
    def edit_height(self) -> Optional[String]:
        """Get editHeight (Pythonic accessor)."""
        return self._editHeight

    @edit_height.setter
    def edit_height(self, value: Optional[String]) -> None:
        """
        Set editHeight with validation.
        
        Args:
            value: The editHeight to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._editHeight = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"editHeight must be String or str or None, got {type(value).__name__}"
            )
        self._editHeight = value
        self._editscale: Optional[String] = None

    @property
    def editscale(self) -> Optional[String]:
        """Get editscale (Pythonic accessor)."""
        return self._editscale

    @editscale.setter
    def editscale(self, value: Optional[String]) -> None:
        """
        Set editscale with validation.
        
        Args:
            value: The editscale to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._editscale = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"editscale must be String or str or None, got {type(value).__name__}"
            )
        self._editscale = value
                # added to the number in the units are: cm, mm, px, pt.
        # The default unit.
        self._editWidth: Optional[String] = None

    @property
    def edit_width(self) -> Optional[String]:
        """Get editWidth (Pythonic accessor)."""
        return self._editWidth

    @edit_width.setter
    def edit_width(self, value: Optional[String]) -> None:
        """
        Set editWidth with validation.
        
        Args:
            value: The editWidth to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._editWidth = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"editWidth must be String or str or None, got {type(value).__name__}"
            )
        self._editWidth = value
        # This attribute is ASAM FSX and kept in AUTOSAR in order cut and paste.
        self._filename: Optional[String] = None

    @property
    def filename(self) -> Optional[String]:
        """Get filename (Pythonic accessor)."""
        return self._filename

    @filename.setter
    def filename(self, value: Optional[String]) -> None:
        """
        Set filename with validation.
        
        Args:
            value: The filename to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._filename = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"filename must be String or str or None, got {type(value).__name__}"
            )
        self._filename = value
                # , to insert a graphic in its is adapted, if it is too big for the space for
                # was intended.
        # Default is "AS-IS" 535 Document ID 202:
                # AUTOSAR_FO_TPS_GenericStructureTemplate Template R23-11.
        self._fit: Optional[GraphicFitEnum] = None

    @property
    def fit(self) -> Optional[GraphicFitEnum]:
        """Get fit (Pythonic accessor)."""
        return self._fit

    @fit.setter
    def fit(self, value: Optional[GraphicFitEnum]) -> None:
        """
        Set fit with validation.
        
        Args:
            value: The fit to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._fit = None
            return

        if not isinstance(value, GraphicFitEnum):
            raise TypeError(
                f"fit must be GraphicFitEnum or None, got {type(value).__name__}"
            )
        self._fit = value
        # is that when editing a documentation, a figure delivered by the modeling
                # tool) is inserted by the as reference (this is the role of graphic).
        # real figure maybe injected during document be able to recognize this
                # situation, this be applied.
        self._generator: Optional[NameToken] = None

    @property
    def generator(self) -> Optional[NameToken]:
        """Get generator (Pythonic accessor)."""
        return self._generator

    @generator.setter
    def generator(self, value: Optional[NameToken]) -> None:
        """
        Set generator with validation.
        
        Args:
            value: The generator to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._generator = None
            return

        if not isinstance(value, (NameToken, str)):
            raise TypeError(
                f"generator must be NameToken or str or None, got {type(value).__name__}"
            )
        self._generator = value
        # The unit can be the number in the string.
        # Possible units are: cm, pt.
        # The default unit is px.
        self._height: Optional[String] = None

    @property
    def height(self) -> Optional[String]:
        """Get height (Pythonic accessor)."""
        return self._height

    @height.setter
    def height(self, value: Optional[String]) -> None:
        """
        Set height with validation.
        
        Args:
            value: The height to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._height = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"height must be String or str or None, got {type(value).__name__}"
            )
        self._height = value
        # Default is AS-IS.
        self._htmlFit: Optional[GraphicFitEnum] = None

    @property
    def html_fit(self) -> Optional[GraphicFitEnum]:
        """Get htmlFit (Pythonic accessor)."""
        return self._htmlFit

    @html_fit.setter
    def html_fit(self, value: Optional[GraphicFitEnum]) -> None:
        """
        Set htmlFit with validation.
        
        Args:
            value: The htmlFit to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._htmlFit = None
            return

        if not isinstance(value, GraphicFitEnum):
            raise TypeError(
                f"htmlFit must be GraphicFitEnum or None, got {type(value).__name__}"
            )
        self._htmlFit = value
                # the number in the string.
        # are: cm, mm, px, pt.
        # The default unit is px.
        self._htmlHeight: Optional[String] = None

    @property
    def html_height(self) -> Optional[String]:
        """Get htmlHeight (Pythonic accessor)."""
        return self._htmlHeight

    @html_height.setter
    def html_height(self, value: Optional[String]) -> None:
        """
        Set htmlHeight with validation.
        
        Args:
            value: The htmlHeight to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._htmlHeight = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"htmlHeight must be String or str or None, got {type(value).__name__}"
            )
        self._htmlHeight = value
        self._htmlScale: Optional[String] = None

    @property
    def html_scale(self) -> Optional[String]:
        """Get htmlScale (Pythonic accessor)."""
        return self._htmlScale

    @html_scale.setter
    def html_scale(self, value: Optional[String]) -> None:
        """
        Set htmlScale with validation.
        
        Args:
            value: The htmlScale to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._htmlScale = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"htmlScale must be String or str or None, got {type(value).__name__}"
            )
        self._htmlScale = value
                # the number in the string.
        # are: cm, mm, px, pt.
        # The default unit is px.
        self._htmlWidth: Optional[String] = None

    @property
    def html_width(self) -> Optional[String]:
        """Get htmlWidth (Pythonic accessor)."""
        return self._htmlWidth

    @html_width.setter
    def html_width(self, value: Optional[String]) -> None:
        """
        Set htmlWidth with validation.
        
        Args:
            value: The htmlWidth to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._htmlWidth = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"htmlWidth must be String or str or None, got {type(value).__name__}"
            )
        self._htmlWidth = value
        self._notation: Optional[GraphicNotationEnum] = None

    @property
    def notation(self) -> Optional[GraphicNotationEnum]:
        """Get notation (Pythonic accessor)."""
        return self._notation

    @notation.setter
    def notation(self, value: Optional[GraphicNotationEnum]) -> None:
        """
        Set notation with validation.
        
        Args:
            value: The notation to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._notation = None
            return

        if not isinstance(value, GraphicNotationEnum):
            raise TypeError(
                f"notation must be GraphicNotationEnum or None, got {type(value).__name__}"
            )
        self._notation = value
        self._scale: Optional[String] = None

    @property
    def scale(self) -> Optional[String]:
        """Get scale (Pythonic accessor)."""
        return self._scale

    @scale.setter
    def scale(self, value: Optional[String]) -> None:
        """
        Set scale with validation.
        
        Args:
            value: The scale to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._scale = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"scale must be String or str or None, got {type(value).__name__}"
            )
        self._scale = value
        # The unit can be the number in the string.
        # Possible units are: cm, pt.
        # The default unit is px.
        self._width: Optional[String] = None

    @property
    def width(self) -> Optional[String]:
        """Get width (Pythonic accessor)."""
        return self._width

    @width.setter
    def width(self, value: Optional[String]) -> None:
        """
        Set width with validation.
        
        Args:
            value: The width to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._width = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"width must be String or str or None, got {type(value).__name__}"
            )
        self._width = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEditfit(self) -> GraphicFitEnum:
        """
        AUTOSAR-compliant getter for editfit.
        
        Returns:
            The editfit value
        
        Note:
            Delegates to editfit property (CODING_RULE_V2_00017)
        """
        return self.editfit  # Delegates to property

    def setEditfit(self, value: GraphicFitEnum) -> Graphic:
        """
        AUTOSAR-compliant setter for editfit with method chaining.
        
        Args:
            value: The editfit to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to editfit property setter (gets validation automatically)
        """
        self.editfit = value  # Delegates to property setter
        return self

    def getEditHeight(self) -> String:
        """
        AUTOSAR-compliant getter for editHeight.
        
        Returns:
            The editHeight value
        
        Note:
            Delegates to edit_height property (CODING_RULE_V2_00017)
        """
        return self.edit_height  # Delegates to property

    def setEditHeight(self, value: String) -> Graphic:
        """
        AUTOSAR-compliant setter for editHeight with method chaining.
        
        Args:
            value: The editHeight to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to edit_height property setter (gets validation automatically)
        """
        self.edit_height = value  # Delegates to property setter
        return self

    def getEditscale(self) -> String:
        """
        AUTOSAR-compliant getter for editscale.
        
        Returns:
            The editscale value
        
        Note:
            Delegates to editscale property (CODING_RULE_V2_00017)
        """
        return self.editscale  # Delegates to property

    def setEditscale(self, value: String) -> Graphic:
        """
        AUTOSAR-compliant setter for editscale with method chaining.
        
        Args:
            value: The editscale to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to editscale property setter (gets validation automatically)
        """
        self.editscale = value  # Delegates to property setter
        return self

    def getEditWidth(self) -> String:
        """
        AUTOSAR-compliant getter for editWidth.
        
        Returns:
            The editWidth value
        
        Note:
            Delegates to edit_width property (CODING_RULE_V2_00017)
        """
        return self.edit_width  # Delegates to property

    def setEditWidth(self, value: String) -> Graphic:
        """
        AUTOSAR-compliant setter for editWidth with method chaining.
        
        Args:
            value: The editWidth to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to edit_width property setter (gets validation automatically)
        """
        self.edit_width = value  # Delegates to property setter
        return self

    def getFilename(self) -> String:
        """
        AUTOSAR-compliant getter for filename.
        
        Returns:
            The filename value
        
        Note:
            Delegates to filename property (CODING_RULE_V2_00017)
        """
        return self.filename  # Delegates to property

    def setFilename(self, value: String) -> Graphic:
        """
        AUTOSAR-compliant setter for filename with method chaining.
        
        Args:
            value: The filename to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to filename property setter (gets validation automatically)
        """
        self.filename = value  # Delegates to property setter
        return self

    def getFit(self) -> GraphicFitEnum:
        """
        AUTOSAR-compliant getter for fit.
        
        Returns:
            The fit value
        
        Note:
            Delegates to fit property (CODING_RULE_V2_00017)
        """
        return self.fit  # Delegates to property

    def setFit(self, value: GraphicFitEnum) -> Graphic:
        """
        AUTOSAR-compliant setter for fit with method chaining.
        
        Args:
            value: The fit to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to fit property setter (gets validation automatically)
        """
        self.fit = value  # Delegates to property setter
        return self

    def getGenerator(self) -> NameToken:
        """
        AUTOSAR-compliant getter for generator.
        
        Returns:
            The generator value
        
        Note:
            Delegates to generator property (CODING_RULE_V2_00017)
        """
        return self.generator  # Delegates to property

    def setGenerator(self, value: NameToken) -> Graphic:
        """
        AUTOSAR-compliant setter for generator with method chaining.
        
        Args:
            value: The generator to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to generator property setter (gets validation automatically)
        """
        self.generator = value  # Delegates to property setter
        return self

    def getHeight(self) -> String:
        """
        AUTOSAR-compliant getter for height.
        
        Returns:
            The height value
        
        Note:
            Delegates to height property (CODING_RULE_V2_00017)
        """
        return self.height  # Delegates to property

    def setHeight(self, value: String) -> Graphic:
        """
        AUTOSAR-compliant setter for height with method chaining.
        
        Args:
            value: The height to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to height property setter (gets validation automatically)
        """
        self.height = value  # Delegates to property setter
        return self

    def getHtmlFit(self) -> GraphicFitEnum:
        """
        AUTOSAR-compliant getter for htmlFit.
        
        Returns:
            The htmlFit value
        
        Note:
            Delegates to html_fit property (CODING_RULE_V2_00017)
        """
        return self.html_fit  # Delegates to property

    def setHtmlFit(self, value: GraphicFitEnum) -> Graphic:
        """
        AUTOSAR-compliant setter for htmlFit with method chaining.
        
        Args:
            value: The htmlFit to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to html_fit property setter (gets validation automatically)
        """
        self.html_fit = value  # Delegates to property setter
        return self

    def getHtmlHeight(self) -> String:
        """
        AUTOSAR-compliant getter for htmlHeight.
        
        Returns:
            The htmlHeight value
        
        Note:
            Delegates to html_height property (CODING_RULE_V2_00017)
        """
        return self.html_height  # Delegates to property

    def setHtmlHeight(self, value: String) -> Graphic:
        """
        AUTOSAR-compliant setter for htmlHeight with method chaining.
        
        Args:
            value: The htmlHeight to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to html_height property setter (gets validation automatically)
        """
        self.html_height = value  # Delegates to property setter
        return self

    def getHtmlScale(self) -> String:
        """
        AUTOSAR-compliant getter for htmlScale.
        
        Returns:
            The htmlScale value
        
        Note:
            Delegates to html_scale property (CODING_RULE_V2_00017)
        """
        return self.html_scale  # Delegates to property

    def setHtmlScale(self, value: String) -> Graphic:
        """
        AUTOSAR-compliant setter for htmlScale with method chaining.
        
        Args:
            value: The htmlScale to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to html_scale property setter (gets validation automatically)
        """
        self.html_scale = value  # Delegates to property setter
        return self

    def getHtmlWidth(self) -> String:
        """
        AUTOSAR-compliant getter for htmlWidth.
        
        Returns:
            The htmlWidth value
        
        Note:
            Delegates to html_width property (CODING_RULE_V2_00017)
        """
        return self.html_width  # Delegates to property

    def setHtmlWidth(self, value: String) -> Graphic:
        """
        AUTOSAR-compliant setter for htmlWidth with method chaining.
        
        Args:
            value: The htmlWidth to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to html_width property setter (gets validation automatically)
        """
        self.html_width = value  # Delegates to property setter
        return self

    def getNotation(self) -> GraphicNotationEnum:
        """
        AUTOSAR-compliant getter for notation.
        
        Returns:
            The notation value
        
        Note:
            Delegates to notation property (CODING_RULE_V2_00017)
        """
        return self.notation  # Delegates to property

    def setNotation(self, value: GraphicNotationEnum) -> Graphic:
        """
        AUTOSAR-compliant setter for notation with method chaining.
        
        Args:
            value: The notation to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to notation property setter (gets validation automatically)
        """
        self.notation = value  # Delegates to property setter
        return self

    def getScale(self) -> String:
        """
        AUTOSAR-compliant getter for scale.
        
        Returns:
            The scale value
        
        Note:
            Delegates to scale property (CODING_RULE_V2_00017)
        """
        return self.scale  # Delegates to property

    def setScale(self, value: String) -> Graphic:
        """
        AUTOSAR-compliant setter for scale with method chaining.
        
        Args:
            value: The scale to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to scale property setter (gets validation automatically)
        """
        self.scale = value  # Delegates to property setter
        return self

    def getWidth(self) -> String:
        """
        AUTOSAR-compliant getter for width.
        
        Returns:
            The width value
        
        Note:
            Delegates to width property (CODING_RULE_V2_00017)
        """
        return self.width  # Delegates to property

    def setWidth(self, value: String) -> Graphic:
        """
        AUTOSAR-compliant setter for width with method chaining.
        
        Args:
            value: The width to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to width property setter (gets validation automatically)
        """
        self.width = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_editfit(self, value: Optional[GraphicFitEnum]) -> Graphic:
        """
        Set editfit and return self for chaining.
        
        Args:
            value: The editfit to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_editfit("value")
        """
        self.editfit = value  # Use property setter (gets validation)
        return self

    def with_edit_height(self, value: Optional[String]) -> Graphic:
        """
        Set editHeight and return self for chaining.
        
        Args:
            value: The editHeight to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_edit_height("value")
        """
        self.edit_height = value  # Use property setter (gets validation)
        return self

    def with_editscale(self, value: Optional[String]) -> Graphic:
        """
        Set editscale and return self for chaining.
        
        Args:
            value: The editscale to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_editscale("value")
        """
        self.editscale = value  # Use property setter (gets validation)
        return self

    def with_edit_width(self, value: Optional[String]) -> Graphic:
        """
        Set editWidth and return self for chaining.
        
        Args:
            value: The editWidth to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_edit_width("value")
        """
        self.edit_width = value  # Use property setter (gets validation)
        return self

    def with_filename(self, value: Optional[String]) -> Graphic:
        """
        Set filename and return self for chaining.
        
        Args:
            value: The filename to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_filename("value")
        """
        self.filename = value  # Use property setter (gets validation)
        return self

    def with_fit(self, value: Optional[GraphicFitEnum]) -> Graphic:
        """
        Set fit and return self for chaining.
        
        Args:
            value: The fit to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_fit("value")
        """
        self.fit = value  # Use property setter (gets validation)
        return self

    def with_generator(self, value: Optional[NameToken]) -> Graphic:
        """
        Set generator and return self for chaining.
        
        Args:
            value: The generator to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_generator("value")
        """
        self.generator = value  # Use property setter (gets validation)
        return self

    def with_height(self, value: Optional[String]) -> Graphic:
        """
        Set height and return self for chaining.
        
        Args:
            value: The height to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_height("value")
        """
        self.height = value  # Use property setter (gets validation)
        return self

    def with_html_fit(self, value: Optional[GraphicFitEnum]) -> Graphic:
        """
        Set htmlFit and return self for chaining.
        
        Args:
            value: The htmlFit to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_html_fit("value")
        """
        self.html_fit = value  # Use property setter (gets validation)
        return self

    def with_html_height(self, value: Optional[String]) -> Graphic:
        """
        Set htmlHeight and return self for chaining.
        
        Args:
            value: The htmlHeight to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_html_height("value")
        """
        self.html_height = value  # Use property setter (gets validation)
        return self

    def with_html_scale(self, value: Optional[String]) -> Graphic:
        """
        Set htmlScale and return self for chaining.
        
        Args:
            value: The htmlScale to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_html_scale("value")
        """
        self.html_scale = value  # Use property setter (gets validation)
        return self

    def with_html_width(self, value: Optional[String]) -> Graphic:
        """
        Set htmlWidth and return self for chaining.
        
        Args:
            value: The htmlWidth to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_html_width("value")
        """
        self.html_width = value  # Use property setter (gets validation)
        return self

    def with_notation(self, value: Optional[GraphicNotationEnum]) -> Graphic:
        """
        Set notation and return self for chaining.
        
        Args:
            value: The notation to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_notation("value")
        """
        self.notation = value  # Use property setter (gets validation)
        return self

    def with_scale(self, value: Optional[String]) -> Graphic:
        """
        Set scale and return self for chaining.
        
        Args:
            value: The scale to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_scale("value")
        """
        self.scale = value  # Use property setter (gets validation)
        return self

    def with_width(self, value: Optional[String]) -> Graphic:
        """
        Set width and return self for chaining.
        
        Args:
            value: The width to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_width("value")
        """
        self.width = value  # Use property setter (gets validation)
        return self



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
        self._area: Area = None

    @property
    def area(self) -> Area:
        """Get area (Pythonic accessor)."""
        return self._area

    @area.setter
    def area(self, value: Area) -> None:
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
        # Any number of elements may be assigned class name or set of class names.
        # Multiple shall be separated by white space names are typically used to apply
                # CSS to an element.
        self._class_name: Optional[String] = None

    @property
    def class_name(self) -> Optional[String]:
        """Get class_name (Pythonic accessor)."""
        return self._class_name

    @class_name.setter
    def class_name(self, value: Optional[String]) -> None:
        """
        Set class_name with validation.
        
        Args:
            value: The class_name to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._class_name = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"class_name must be String or str or None, got {type(value).__name__}"
            )
        self._class_name = value
                # to be referenced in image through the attribute USEMAP.
        # Although not actually necessary in the MSR model, it was order to support the
                # MAPs which were created.
        self._name: Optional[NameToken] = None

    @property
    def name(self) -> Optional[NameToken]:
        """Get name (Pythonic accessor)."""
        return self._name

    @name.setter
    def name(self, value: Optional[NameToken]) -> None:
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

        if not isinstance(value, (NameToken, str)):
            raise TypeError(
                f"name must be NameToken or str or None, got {type(value).__name__}"
            )
        self._name = value
        # this attribute to be the Event.
        self._onclick: Optional[String] = None

    @property
    def onclick(self) -> Optional[String]:
        """Get onclick (Pythonic accessor)."""
        return self._onclick

    @onclick.setter
    def onclick(self, value: Optional[String]) -> None:
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

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"onclick must be String or str or None, got {type(value).__name__}"
            )
        self._onclick = value
                # in this attribute performed in the Event.
        # 535 Document ID 202: AUTOSAR_FO_TPS_GenericStructureTemplate Template R23-11.
        self._ondblclick: Optional[String] = None

    @property
    def ondblclick(self) -> Optional[String]:
        """Get ondblclick (Pythonic accessor)."""
        return self._ondblclick

    @ondblclick.setter
    def ondblclick(self, value: Optional[String]) -> None:
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

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"ondblclick must be String or str or None, got {type(value).__name__}"
            )
        self._ondblclick = value
        # can be stored in this attribute to be performed in.
        self._onkeydown: Optional[String] = None

    @property
    def onkeydown(self) -> Optional[String]:
        """Get onkeydown (Pythonic accessor)."""
        return self._onkeydown

    @onkeydown.setter
    def onkeydown(self, value: Optional[String]) -> None:
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

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"onkeydown must be String or str or None, got {type(value).__name__}"
            )
        self._onkeydown = value
        # can be stored in this attribute to be performed in.
        self._onkeypress: Optional[String] = None

    @property
    def onkeypress(self) -> Optional[String]:
        """Get onkeypress (Pythonic accessor)."""
        return self._onkeypress

    @onkeypress.setter
    def onkeypress(self, value: Optional[String]) -> None:
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

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"onkeypress must be String or str or None, got {type(value).__name__}"
            )
        self._onkeypress = value
        # can be stored in this attribute to be performed in.
        self._onkeyup: Optional[String] = None

    @property
    def onkeyup(self) -> Optional[String]:
        """Get onkeyup (Pythonic accessor)."""
        return self._onkeyup

    @onkeyup.setter
    def onkeyup(self, value: Optional[String]) -> None:
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

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"onkeyup must be String or str or None, got {type(value).__name__}"
            )
        self._onkeyup = value
                # the current element.
        # can be stored in this attribute to be performed in.
        self._onmousedown: Optional[String] = None

    @property
    def onmousedown(self) -> Optional[String]:
        """Get onmousedown (Pythonic accessor)."""
        return self._onmousedown

    @onmousedown.setter
    def onmousedown(self, value: Optional[String]) -> None:
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

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"onmousedown must be String or str or None, got {type(value).__name__}"
            )
        self._onmousedown = value
        # e.
        # it is located on the can be stored in this attribute to be performed in.
        self._onmousemove: Optional[String] = None

    @property
    def onmousemove(self) -> Optional[String]:
        """Get onmousemove (Pythonic accessor)."""
        return self._onmousemove

    @onmousemove.setter
    def onmousemove(self, value: Optional[String]) -> None:
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

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"onmousemove must be String or str or None, got {type(value).__name__}"
            )
        self._onmousemove = value
        # can be stored in this attribute to be performed in.
        self._onmouseout: Optional[String] = None

    @property
    def onmouseout(self) -> Optional[String]:
        """Get onmouseout (Pythonic accessor)."""
        return self._onmouseout

    @onmouseout.setter
    def onmouseout(self, value: Optional[String]) -> None:
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

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"onmouseout must be String or str or None, got {type(value).__name__}"
            )
        self._onmouseout = value
        # from another location can be stored in this attribute to be performed in.
        self._onmouseover: Optional[String] = None

    @property
    def onmouseover(self) -> Optional[String]:
        """Get onmouseover (Pythonic accessor)."""
        return self._onmouseover

    @onmouseover.setter
    def onmouseover(self, value: Optional[String]) -> None:
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

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"onmouseover must be String or str or None, got {type(value).__name__}"
            )
        self._onmouseover = value
                # current element.
        # can be stored in this attribute to be performed in.
        self._onmouseup: Optional[String] = None

    @property
    def onmouseup(self) -> Optional[String]:
        """Get onmouseup (Pythonic accessor)."""
        return self._onmouseup

    @onmouseup.setter
    def onmouseup(self, value: Optional[String]) -> None:
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

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"onmouseup must be String or str or None, got {type(value).__name__}"
            )
        self._onmouseup = value
        # Some Web display this information as tooltips.
        # may make this information available to additional information about the
                # element.
        self._title: Optional[String] = None

    @property
    def title(self) -> Optional[String]:
        """Get title (Pythonic accessor)."""
        return self._title

    @title.setter
    def title(self, value: Optional[String]) -> None:
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

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"title must be String or str or None, got {type(value).__name__}"
            )
        self._title = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getArea(self) -> Area:
        """
        AUTOSAR-compliant getter for area.
        
        Returns:
            The area value
        
        Note:
            Delegates to area property (CODING_RULE_V2_00017)
        """
        return self.area  # Delegates to property

    def setArea(self, value: Area) -> Map:
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

    def getClass(self) -> String:
        """
        AUTOSAR-compliant getter for class.
        
        Returns:
            The class value
        
        Note:
            Delegates to class_name property (CODING_RULE_V2_00017)
        """
        return self.class_name  # Delegates to property

    def setClass(self, value: String) -> Map:
        """
        AUTOSAR-compliant setter for class_name with method chaining.

        Args:
            value: The class_name to set

        Returns:
            self for method chaining

        Note:
            Delegates to class_name property setter (gets validation automatically)
        """
        self.class_name = value  # Delegates to property setter
        return self

    def getName(self) -> NameToken:
        """
        AUTOSAR-compliant getter for name.
        
        Returns:
            The name value
        
        Note:
            Delegates to name property (CODING_RULE_V2_00017)
        """
        return self.name  # Delegates to property

    def setName(self, value: NameToken) -> Map:
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

    def getOnclick(self) -> String:
        """
        AUTOSAR-compliant getter for onclick.
        
        Returns:
            The onclick value
        
        Note:
            Delegates to onclick property (CODING_RULE_V2_00017)
        """
        return self.onclick  # Delegates to property

    def setOnclick(self, value: String) -> Map:
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

    def getOndblclick(self) -> String:
        """
        AUTOSAR-compliant getter for ondblclick.
        
        Returns:
            The ondblclick value
        
        Note:
            Delegates to ondblclick property (CODING_RULE_V2_00017)
        """
        return self.ondblclick  # Delegates to property

    def setOndblclick(self, value: String) -> Map:
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

    def getOnkeydown(self) -> String:
        """
        AUTOSAR-compliant getter for onkeydown.
        
        Returns:
            The onkeydown value
        
        Note:
            Delegates to onkeydown property (CODING_RULE_V2_00017)
        """
        return self.onkeydown  # Delegates to property

    def setOnkeydown(self, value: String) -> Map:
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

    def getOnkeypress(self) -> String:
        """
        AUTOSAR-compliant getter for onkeypress.
        
        Returns:
            The onkeypress value
        
        Note:
            Delegates to onkeypress property (CODING_RULE_V2_00017)
        """
        return self.onkeypress  # Delegates to property

    def setOnkeypress(self, value: String) -> Map:
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

    def getOnkeyup(self) -> String:
        """
        AUTOSAR-compliant getter for onkeyup.
        
        Returns:
            The onkeyup value
        
        Note:
            Delegates to onkeyup property (CODING_RULE_V2_00017)
        """
        return self.onkeyup  # Delegates to property

    def setOnkeyup(self, value: String) -> Map:
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

    def getOnmousedown(self) -> String:
        """
        AUTOSAR-compliant getter for onmousedown.
        
        Returns:
            The onmousedown value
        
        Note:
            Delegates to onmousedown property (CODING_RULE_V2_00017)
        """
        return self.onmousedown  # Delegates to property

    def setOnmousedown(self, value: String) -> Map:
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

    def getOnmousemove(self) -> String:
        """
        AUTOSAR-compliant getter for onmousemove.
        
        Returns:
            The onmousemove value
        
        Note:
            Delegates to onmousemove property (CODING_RULE_V2_00017)
        """
        return self.onmousemove  # Delegates to property

    def setOnmousemove(self, value: String) -> Map:
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

    def getOnmouseout(self) -> String:
        """
        AUTOSAR-compliant getter for onmouseout.
        
        Returns:
            The onmouseout value
        
        Note:
            Delegates to onmouseout property (CODING_RULE_V2_00017)
        """
        return self.onmouseout  # Delegates to property

    def setOnmouseout(self, value: String) -> Map:
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

    def getOnmouseover(self) -> String:
        """
        AUTOSAR-compliant getter for onmouseover.
        
        Returns:
            The onmouseover value
        
        Note:
            Delegates to onmouseover property (CODING_RULE_V2_00017)
        """
        return self.onmouseover  # Delegates to property

    def setOnmouseover(self, value: String) -> Map:
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

    def getOnmouseup(self) -> String:
        """
        AUTOSAR-compliant getter for onmouseup.
        
        Returns:
            The onmouseup value
        
        Note:
            Delegates to onmouseup property (CODING_RULE_V2_00017)
        """
        return self.onmouseup  # Delegates to property

    def setOnmouseup(self, value: String) -> Map:
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

    def getTitle(self) -> String:
        """
        AUTOSAR-compliant getter for title.
        
        Returns:
            The title value
        
        Note:
            Delegates to title property (CODING_RULE_V2_00017)
        """
        return self.title  # Delegates to property

    def setTitle(self, value: String) -> Map:
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

    def with_area(self, value: Area) -> Map:
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

    def with_class_name(self, value: Optional[String]) -> Map:
        """
        Set class_name and return self for chaining.
        
        Args:
            value: The class_name to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_class_name("value")
        """
        self.class_name = value  # Use property setter (gets validation)
        return self

    def with_name(self, value: Optional[NameToken]) -> Map:
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

    def with_onclick(self, value: Optional[String]) -> Map:
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

    def with_ondblclick(self, value: Optional[String]) -> Map:
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

    def with_onkeydown(self, value: Optional[String]) -> Map:
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

    def with_onkeypress(self, value: Optional[String]) -> Map:
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

    def with_onkeyup(self, value: Optional[String]) -> Map:
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

    def with_onmousedown(self, value: Optional[String]) -> Map:
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

    def with_onmousemove(self, value: Optional[String]) -> Map:
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

    def with_onmouseout(self, value: Optional[String]) -> Map:
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

    def with_onmouseover(self, value: Optional[String]) -> Map:
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

    def with_onmouseup(self, value: Optional[String]) -> Map:
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

    def with_title(self, value: Optional[String]) -> Map:
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



class MlFigure(Paginateable):
    """
    This metaclass represents the ability to embed a figure.
    
    Package: M2::MSR::Documentation::BlockElements::Figure::MlFigure
    
    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 307, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This element specifies the title of an illustration.
        self._figureCaption: Optional["Caption"] = None

    @property
    def figure_caption(self) -> Optional["Caption"]:
        """Get figureCaption (Pythonic accessor)."""
        return self._figureCaption

    @figure_caption.setter
    def figure_caption(self, value: Optional["Caption"]) -> None:
        """
        Set figureCaption with validation.
        
        Args:
            value: The figureCaption to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._figureCaption = None
            return

        if not isinstance(value, Caption):
            raise TypeError(
                f"figureCaption must be Caption or None, got {type(value).__name__}"
            )
        self._figureCaption = value
        # It can following values: - Border at the top of the figure - Border at the
                # bottom of the figure - Borders at the top and bottom of the figure - Borders
                # all around the figure - Borders at the sides of the figure - No borders
                # around the figure.
        self._frame: Optional["FrameEnum"] = None

    @property
    def frame(self) -> Optional["FrameEnum"]:
        """Get frame (Pythonic accessor)."""
        return self._frame

    @frame.setter
    def frame(self, value: Optional["FrameEnum"]) -> None:
        """
        Set frame with validation.
        
        Args:
            value: The frame to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._frame = None
            return

        if not isinstance(value, FrameEnum):
            raise TypeError(
                f"frame must be FrameEnum or None, got {type(value).__name__}"
            )
        self._frame = value
                # class.
        # The syntax shall be the applied help system respectively help.
        self._helpEntry: Optional[String] = None

    @property
    def help_entry(self) -> Optional[String]:
        """Get helpEntry (Pythonic accessor)."""
        return self._helpEntry

    @help_entry.setter
    def help_entry(self, value: Optional[String]) -> None:
        """
        Set helpEntry with validation.
        
        Args:
            value: The helpEntry to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._helpEntry = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"helpEntry must be String or str or None, got {type(value).__name__}"
            )
        self._helpEntry = value
        # language.
        self._lGraphic: List[LGraphic] = []

    @property
    def l_graphic(self) -> List[LGraphic]:
        """Get lGraphic (Pythonic accessor)."""
        return self._lGraphic
        # Used to indicate wether the figure should take the width (value = "pgwide")
        # or not (value =.
        self._pgwide: Optional["PgwideEnum"] = None

    @property
    def pgwide(self) -> Optional["PgwideEnum"]:
        """Get pgwide (Pythonic accessor)."""
        return self._pgwide

    @pgwide.setter
    def pgwide(self, value: Optional["PgwideEnum"]) -> None:
        """
        Set pgwide with validation.
        
        Args:
            value: The pgwide to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._pgwide = None
            return

        if not isinstance(value, PgwideEnum):
            raise TypeError(
                f"pgwide must be PgwideEnum or None, got {type(value).__name__}"
            )
        self._pgwide = value
        # This enables to be carried out, which can even be simple devices.
        # Behavior is the same as HTML.
        self._verbatim: Optional["MultiLanguageVerbatim"] = None

    @property
    def verbatim(self) -> Optional["MultiLanguageVerbatim"]:
        """Get verbatim (Pythonic accessor)."""
        return self._verbatim

    @verbatim.setter
    def verbatim(self, value: Optional["MultiLanguageVerbatim"]) -> None:
        """
        Set verbatim with validation.
        
        Args:
            value: The verbatim to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._verbatim = None
            return

        if not isinstance(value, MultiLanguageVerbatim):
            raise TypeError(
                f"verbatim must be MultiLanguageVerbatim or None, got {type(value).__name__}"
            )
        self._verbatim = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getFigureCaption(self) -> "Caption":
        """
        AUTOSAR-compliant getter for figureCaption.
        
        Returns:
            The figureCaption value
        
        Note:
            Delegates to figure_caption property (CODING_RULE_V2_00017)
        """
        return self.figure_caption  # Delegates to property

    def setFigureCaption(self, value: "Caption") -> MlFigure:
        """
        AUTOSAR-compliant setter for figureCaption with method chaining.
        
        Args:
            value: The figureCaption to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to figure_caption property setter (gets validation automatically)
        """
        self.figure_caption = value  # Delegates to property setter
        return self

    def getFrame(self) -> "FrameEnum":
        """
        AUTOSAR-compliant getter for frame.
        
        Returns:
            The frame value
        
        Note:
            Delegates to frame property (CODING_RULE_V2_00017)
        """
        return self.frame  # Delegates to property

    def setFrame(self, value: "FrameEnum") -> MlFigure:
        """
        AUTOSAR-compliant setter for frame with method chaining.
        
        Args:
            value: The frame to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to frame property setter (gets validation automatically)
        """
        self.frame = value  # Delegates to property setter
        return self

    def getHelpEntry(self) -> String:
        """
        AUTOSAR-compliant getter for helpEntry.
        
        Returns:
            The helpEntry value
        
        Note:
            Delegates to help_entry property (CODING_RULE_V2_00017)
        """
        return self.help_entry  # Delegates to property

    def setHelpEntry(self, value: String) -> MlFigure:
        """
        AUTOSAR-compliant setter for helpEntry with method chaining.
        
        Args:
            value: The helpEntry to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to help_entry property setter (gets validation automatically)
        """
        self.help_entry = value  # Delegates to property setter
        return self

    def getLGraphic(self) -> List[LGraphic]:
        """
        AUTOSAR-compliant getter for lGraphic.
        
        Returns:
            The lGraphic value
        
        Note:
            Delegates to l_graphic property (CODING_RULE_V2_00017)
        """
        return self.l_graphic  # Delegates to property

    def getPgwide(self) -> PgwideEnum:
        """
        AUTOSAR-compliant getter for pgwide.
        
        Returns:
            The pgwide value
        
        Note:
            Delegates to pgwide property (CODING_RULE_V2_00017)
        """
        return self.pgwide  # Delegates to property

    def setPgwide(self, value: PgwideEnum) -> MlFigure:
        """
        AUTOSAR-compliant setter for pgwide with method chaining.
        
        Args:
            value: The pgwide to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to pgwide property setter (gets validation automatically)
        """
        self.pgwide = value  # Delegates to property setter
        return self

    def getVerbatim(self) -> "MultiLanguageVerbatim":
        """
        AUTOSAR-compliant getter for verbatim.
        
        Returns:
            The verbatim value
        
        Note:
            Delegates to verbatim property (CODING_RULE_V2_00017)
        """
        return self.verbatim  # Delegates to property

    def setVerbatim(self, value: "MultiLanguageVerbatim") -> MlFigure:
        """
        AUTOSAR-compliant setter for verbatim with method chaining.
        
        Args:
            value: The verbatim to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to verbatim property setter (gets validation automatically)
        """
        self.verbatim = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_figure_caption(self, value: Optional["Caption"]) -> MlFigure:
        """
        Set figureCaption and return self for chaining.
        
        Args:
            value: The figureCaption to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_figure_caption("value")
        """
        self.figure_caption = value  # Use property setter (gets validation)
        return self

    def with_frame(self, value: Optional["FrameEnum"]) -> MlFigure:
        """
        Set frame and return self for chaining.
        
        Args:
            value: The frame to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_frame("value")
        """
        self.frame = value  # Use property setter (gets validation)
        return self

    def with_help_entry(self, value: Optional[String]) -> MlFigure:
        """
        Set helpEntry and return self for chaining.
        
        Args:
            value: The helpEntry to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_help_entry("value")
        """
        self.help_entry = value  # Use property setter (gets validation)
        return self

    def with_pgwide(self, value: Optional["PgwideEnum"]) -> MlFigure:
        """
        Set pgwide and return self for chaining.
        
        Args:
            value: The pgwide to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_pgwide("value")
        """
        self.pgwide = value  # Use property setter (gets validation)
        return self

    def with_verbatim(self, value: Optional["MultiLanguageVerbatim"]) -> MlFigure:
        """
        Set verbatim and return self for chaining.
        
        Args:
            value: The verbatim to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_verbatim("value")
        """
        self.verbatim = value  # Use property setter (gets validation)
        return self



class LGraphic(LanguageSpecific):
    """
    This meta-class represents the figure in one particular language.
    
    Package: M2::MSR::Documentation::BlockElements::Figure::LGraphic
    
    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 307, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to the actual graphic represented in the figure.
        # 535 Document ID 202: AUTOSAR_FO_TPS_GenericStructureTemplate Template R23-11.
        self._graphic: Graphic = None

    @property
    def graphic(self) -> Graphic:
        """Get graphic (Pythonic accessor)."""
        return self._graphic

    @graphic.setter
    def graphic(self, value: Graphic) -> None:
        """
        Set graphic with validation.
        
        Args:
            value: The graphic to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, Graphic):
            raise TypeError(
                f"graphic must be Graphic, got {type(value).__name__}"
            )
        self._graphic = value
        # specific action to each.
        self._map: Optional[Map] = None

    @property
    def map(self) -> Optional[Map]:
        """Get map (Pythonic accessor)."""
        return self._map

    @map.setter
    def map(self, value: Optional[Map]) -> None:
        """
        Set map with validation.
        
        Args:
            value: The map to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._map = None
            return

        if not isinstance(value, Map):
            raise TypeError(
                f"map must be Map or None, got {type(value).__name__}"
            )
        self._map = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getGraphic(self) -> Graphic:
        """
        AUTOSAR-compliant getter for graphic.
        
        Returns:
            The graphic value
        
        Note:
            Delegates to graphic property (CODING_RULE_V2_00017)
        """
        return self.graphic  # Delegates to property

    def setGraphic(self, value: Graphic) -> LGraphic:
        """
        AUTOSAR-compliant setter for graphic with method chaining.
        
        Args:
            value: The graphic to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to graphic property setter (gets validation automatically)
        """
        self.graphic = value  # Delegates to property setter
        return self

    def getMap(self) -> Map:
        """
        AUTOSAR-compliant getter for map.
        
        Returns:
            The map value
        
        Note:
            Delegates to map property (CODING_RULE_V2_00017)
        """
        return self.map  # Delegates to property

    def setMap(self, value: Map) -> LGraphic:
        """
        AUTOSAR-compliant setter for map with method chaining.
        
        Args:
            value: The map to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to map property setter (gets validation automatically)
        """
        self.map = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_graphic(self, value: Graphic) -> LGraphic:
        """
        Set graphic and return self for chaining.
        
        Args:
            value: The graphic to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_graphic("value")
        """
        self.graphic = value  # Use property setter (gets validation)
        return self

    def with_map(self, value: Optional[Map]) -> LGraphic:
        """
        Set map and return self for chaining.
        
        Args:
            value: The map to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_map("value")
        """
        self.map = value  # Use property setter (gets validation)
        return self


class AreaEnumNohref(AREnum):
    """
    AreaEnumNohref enumeration

This enumerator specifies the fact that the area has no reference. Aggregated by Area.nohref

Package: M2::MSR::Documentation::BlockElements::Figure
    """
    # This indicates that the area has no active link.
    nohref = "0"



class AreaEnumShape(AREnum):
    """
    AreaEnumShape enumeration

This enumerator specifies the shape of the area. Aggregated by Area.shape

Package: M2::MSR::Documentation::BlockElements::Figure
    """
    # Structure Template
    Generic = "None"

    # FO R23-11
    AUTOSAR = "None"

    # The shape is a circle.
    circle = "0"

    # This specifies the fact that the area covers the rest of the figure.
    default = "1"

    # The area is specified as polygon.
    poly = "2"

    # The shape is specified as rectangle.
    rect = "3"



class GraphicFitEnum(AREnum):
    """
    GraphicFitEnum enumeration

This enumerator specifies the policy how to place and scale the figure on the page. Aggregated by Graphic.editfit, Graphic.fit, Graphic.htmlFit

Package: M2::MSR::Documentation::BlockElements::Figure
    """
    # This indicates that the image shall be incorporated as is without scaling, rotation etc.
    AsIs = "0"

    # Fit to the page
    FitToPage = "1"

    # Structure Template
    Generic = "None"

    # FO R23-11 FitToText fit to the text containing the graphic.
    AUTOSAR = "2"

    # This indicates that the width of the graphic shall be limited to the page width. The image shall not be scaled down but cropped.
    LimitToPage = "3"

    # This indicates that the width of the graphic shall be limited to the width of the current text flow. The image shall not be scaled down but cropped.
    LimitToText = "4"

    # Rotate 180 degree
    Rotate180Rotate180LimitTo = "5"

    #
    Text = "6"

    # Rotate 90 degree counter clockwise
    Rotate90ccw = "7"

    # Rotate by 90 degree counter clock wise and then fit to text
    Rotate90CcwFitToTextRotate90CcwLimit = "8"

    #
    ToText = "9"

    # Rotate 90 degree clockwise
    Rotate90Cw = "10"

    # Rotate by 90 degree and then fit to text
    Rotate90CwFitToTextRotate90CwLimitTo = "11"

    #
    Text = "12"



class GraphicNotationEnum(AREnum):
    """
    GraphicNotationEnum enumeration

This enumerator specifies the various notations (finally file types) used to represent the figure. Aggregated by Graphic.notation

Package: M2::MSR::Documentation::BlockElements::Figure
    """
    # bitmap image
    bmp = "0"

    # Encapsulated Postscript
    eps = "1"

    # Graphics Interchange Format
    gif = "2"

    # "Joint Photographic Experts Group" format
    jpg = "3"

    # Portable Document Format
    pdf = "4"

    # Portable Network Graphics
    png = "5"

    # Structure Template
    Generic = "None"

    # FO R23-11 svg scalable vector graphic
    AUTOSAR = "6"

    # Tagged Image File Format
    tiff = "7"
