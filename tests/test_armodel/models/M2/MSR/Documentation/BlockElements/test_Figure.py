"""
This module contains tests for the Figure module in MSR.Documentation.BlockElements.
"""

import inspect

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import NameToken, String
from armodel.models.M2.MSR.Documentation.BlockElements.Figure import (
    Area,
    AreaEnumNohref,
    AreaEnumShape,
    Graphic,
    GraphicFitEnum,
    GraphicNotationEnum,
    LGraphic,
    Map,
    MlFigure,
)


class TestGraphicFitEnum:
    """Test class for GraphicFitEnum class."""

    def test_graphic_fit_enum_initialization(self):
        """Test that a GraphicFitEnum object can be initialized."""
        graphic_fit_enum = GraphicFitEnum()
        assert graphic_fit_enum is not None

    def test_graphic_fit_enum_spec_literals(self):
        """GraphicFitEnum shall expose the 13 spec literals with their XSD string values."""
        enum = GraphicFitEnum()
        expected = {
            GraphicFitEnum.ASIS: "AS-IS",
            GraphicFitEnum.FIT_TO_PAGE: "FIT-TO-PAGE",
            GraphicFitEnum.FIT_TO_TEXT: "FIT-TO-TEXT",
            GraphicFitEnum.LIMIT_TO_PAGE: "LIMIT-TO-PAGE",
            GraphicFitEnum.LIMIT_TO_TEXT: "LIMIT-TO-TEXT",
            GraphicFitEnum.ROTATE_180: "ROTATE-180",
            GraphicFitEnum.ROTATE_180_LIMIT_TO_TEXT: "ROTATE-180-LIMIT-TO-TEXT",
            GraphicFitEnum.ROTATE_90CCW: "ROTATE-90-CCW",
            GraphicFitEnum.ROTATE_90CCW_FIT_TO_TEXT: "ROTATE-90-CCW-FIT-TO-TEXT",
            GraphicFitEnum.ROTATE_90CCW_LIMIT_TO_TEXT: "ROTATE-90-CCW-LIMIT-TO-TEXT",
            GraphicFitEnum.ROTATE_90CW: "ROTATE-90-CW",
            GraphicFitEnum.ROTATE_90CW_FIT_TO_TEXT: "ROTATE-90-CW-FIT-TO-TEXT",
            GraphicFitEnum.ROTATE_90CW_LIMIT_TO_TEXT: "ROTATE-90-CW-LIMIT-TO-TEXT",
        }
        for const, value in expected.items():
            assert const == value
        assert set(enum.getEnumValues()) == set(expected.values())


class TestGraphicNotationEnum:
    """Test class for GraphicNotationEnum (AUTOSAR_FO_TPS_GenericStructureTemplate, Table 9.22)."""

    def test_graphic_notation_enum_initialization(self):
        """Test that a GraphicNotationEnum object can be initialized."""
        graphic_notation_enum = GraphicNotationEnum()
        assert graphic_notation_enum is not None
        assert isinstance(graphic_notation_enum, GraphicNotationEnum)

    def test_graphic_notation_enum_spec_literals(self):
        """GraphicNotationEnum shall expose the 8 spec literals with their XSD string values."""
        enum = GraphicNotationEnum()
        expected = {
            GraphicNotationEnum.BMP: "BMP",
            GraphicNotationEnum.EPS: "EPS",
            GraphicNotationEnum.GIF: "GIF",
            GraphicNotationEnum.JPG: "JPG",
            GraphicNotationEnum.PDF: "PDF",
            GraphicNotationEnum.PNG: "PNG",
            GraphicNotationEnum.SVG: "SVG",
            GraphicNotationEnum.TIFF: "TIFF",
        }
        for const, value in expected.items():
            assert const == value
        assert set(enum.getEnumValues()) == set(expected.values())

    def test_graphic_notation_enum_set_get_value(self):
        """setValue/getValue shall round-trip a spec literal."""
        enum = GraphicNotationEnum().setValue(GraphicNotationEnum.SVG)
        assert enum.getValue() == "SVG"

    def test_graphic_notation_enum_validate_enum_value(self):
        """validateEnumValue shall accept the XSD literal values only."""
        enum = GraphicNotationEnum()
        assert enum.validateEnumValue("BMP") is True
        assert enum.validateEnumValue("TIFF") is True
        assert enum.validateEnumValue("bmp") is False


class TestGraphic:
    """Test class for Graphic class."""

    def test_graphic_initialization(self):
        """Test that a Graphic object can be initialized with default values."""
        graphic = Graphic()
        assert graphic.editfit is None
        assert graphic.editHeight is None
        assert graphic.editscale is None
        assert graphic.editWidth is None
        assert graphic.filename is None
        assert graphic.fit is None
        assert graphic.generator is None
        assert graphic.height is None
        assert graphic.htmlFit is None
        assert graphic.htmlHeight is None
        assert graphic.htmlScale is None
        assert graphic.htmlWidth is None
        assert graphic.notation is None
        assert graphic.scale is None
        assert graphic.width is None

    def test_graphic_editfit_methods(self):
        """Test the editfit getter and setter."""
        graphic = Graphic()
        editfit = GraphicFitEnum()

        result = graphic.setEditfit(editfit)
        assert graphic.getEditfit() == editfit
        assert result == graphic

        graphic.setEditfit(None)
        assert graphic.getEditfit() == editfit

    def test_graphic_edit_height_methods(self):
        """Test the editHeight getter and setter."""
        graphic = Graphic()
        height = String()

        result = graphic.setEditHeight(height)
        assert graphic.getEditHeight() == height
        assert result == graphic

        graphic.setEditHeight(None)
        assert graphic.getEditHeight() == height

    def test_graphic_editscale_methods(self):
        """Test the editscale getter and setter."""
        graphic = Graphic()
        scale = String()

        result = graphic.setEditscale(scale)
        assert graphic.getEditscale() == scale
        assert result == graphic

        graphic.setEditscale(None)
        assert graphic.getEditscale() == scale

    def test_graphic_edit_width_methods(self):
        """Test the editWidth getter and setter."""
        graphic = Graphic()
        width = String()

        result = graphic.setEditWidth(width)
        assert graphic.getEditWidth() == width
        assert result == graphic

        graphic.setEditWidth(None)
        assert graphic.getEditWidth() == width

    def test_graphic_filename_methods(self):
        """Test the filename getter and setter."""
        graphic = Graphic()
        filename = String()

        result = graphic.setFilename(filename)
        assert graphic.getFilename() == filename
        assert result == graphic

        graphic.setFilename(None)
        assert graphic.getFilename() == filename

    def test_graphic_fit_methods(self):
        """Test the fit getter and setter."""
        graphic = Graphic()
        fit = GraphicFitEnum()

        result = graphic.setFit(fit)
        assert graphic.getFit() == fit
        assert result == graphic

        graphic.setFit(None)
        assert graphic.getFit() == fit

    def test_graphic_generator_methods(self):
        """Test the generator getter and setter."""
        graphic = Graphic()
        generator = NameToken()

        result = graphic.setGenerator(generator)
        assert graphic.getGenerator() == generator
        assert result == graphic

        graphic.setGenerator(None)
        assert graphic.getGenerator() == generator

    def test_graphic_height_methods(self):
        """Test the height getter and setter."""
        graphic = Graphic()
        height = String()

        result = graphic.setHeight(height)
        assert graphic.getHeight() == height
        assert result == graphic

        graphic.setHeight(None)
        assert graphic.getHeight() == height

    def test_graphic_html_fit_methods(self):
        """Test the htmlFit getter and setter."""
        graphic = Graphic()
        html_fit = GraphicFitEnum()

        result = graphic.setHtmlFit(html_fit)
        assert graphic.getHtmlFit() == html_fit
        assert result == graphic

        graphic.setHtmlFit(None)
        assert graphic.getHtmlFit() == html_fit

    def test_graphic_html_height_methods(self):
        """Test the htmlHeight getter and setter."""
        graphic = Graphic()
        html_height = String()

        result = graphic.setHtmlHeight(html_height)
        assert graphic.getHtmlHeight() == html_height
        assert result == graphic

        graphic.setHtmlHeight(None)
        assert graphic.getHtmlHeight() == html_height

    def test_graphic_html_scale_methods(self):
        """Test the htmlScale getter and setter."""
        graphic = Graphic()
        html_scale = String()

        result = graphic.setHtmlScale(html_scale)
        assert graphic.getHtmlScale() == html_scale
        assert result == graphic

        graphic.setHtmlScale(None)
        assert graphic.getHtmlScale() == html_scale

    def test_graphic_html_width_methods(self):
        """Test the htmlWidth getter and setter."""
        graphic = Graphic()
        html_width = String()

        result = graphic.setHtmlWidth(html_width)
        assert graphic.getHtmlWidth() == html_width
        assert result == graphic

        graphic.setHtmlWidth(None)
        assert graphic.getHtmlWidth() == html_width

    def test_graphic_notation_methods(self):
        """Test the notation getter and setter."""
        graphic = Graphic()
        notation = GraphicNotationEnum()

        result = graphic.setNotation(notation)
        assert graphic.getNotation() == notation
        assert result == graphic

        graphic.setNotation(None)
        assert graphic.getNotation() == notation

    def test_graphic_scale_methods(self):
        """Test the scale getter and setter."""
        graphic = Graphic()
        scale = String()

        result = graphic.setScale(scale)
        assert graphic.getScale() == scale
        assert result == graphic

        graphic.setScale(None)
        assert graphic.getScale() == scale

    def test_graphic_width_methods(self):
        """Test the width getter and setter."""
        graphic = Graphic()
        width = String()

        result = graphic.setWidth(width)
        assert graphic.getWidth() == width
        assert result == graphic

        graphic.setWidth(None)
        assert graphic.getWidth() == width


class TestMap:
    """Test class for Map class (AUTOSAR_FO_TPS_GenericStructureTemplate, Table 9.23)."""

    def test_map_initialization(self):
        """A new Map shall have an empty area list and all attributes unset."""
        map_obj = Map()
        assert map_obj is not None
        assert isinstance(map_obj, Map)
        assert map_obj.getAreas() == []
        assert map_obj.getClass() is None
        assert map_obj.getName() is None
        assert map_obj.getOnclick() is None
        assert map_obj.getOndblclick() is None
        assert map_obj.getOnkeydown() is None
        assert map_obj.getOnkeypress() is None
        assert map_obj.getOnkeyup() is None
        assert map_obj.getOnmousedown() is None
        assert map_obj.getOnmousemove() is None
        assert map_obj.getOnmouseout() is None
        assert map_obj.getOnmouseover() is None
        assert map_obj.getOnmouseup() is None
        assert map_obj.getTitle() is None

    def test_map_add_area(self):
        """addArea shall append Areas in insertion order with chaining."""
        map_obj = Map()
        area1 = Area()
        area2 = Area()

        result = map_obj.addArea(area1)
        assert result is map_obj
        map_obj.addArea(area2)
        assert map_obj.getAreas() == [area1, area2]

    def test_map_class_methods(self):
        """class shall round-trip via set/get with chaining and a None no-op."""
        map_obj = Map()
        value = String().setValue("c1 c2")

        result = map_obj.setClass(value)
        assert result is map_obj
        assert map_obj.getClass() is value

        map_obj.setClass(None)
        assert map_obj.getClass() is value

    def test_map_name_methods(self):
        """name shall round-trip via set/get with chaining and a None no-op."""
        map_obj = Map()
        value = NameToken().setValue("map1")

        result = map_obj.setName(value)
        assert result is map_obj
        assert map_obj.getName() is value

        map_obj.setName(None)
        assert map_obj.getName() is value

    def test_map_onclick_methods(self):
        """onclick shall round-trip via set/get with chaining and a None no-op."""
        map_obj = Map()
        value = String().setValue("click()")

        result = map_obj.setOnclick(value)
        assert result is map_obj
        assert map_obj.getOnclick() is value

        map_obj.setOnclick(None)
        assert map_obj.getOnclick() is value

    def test_map_ondblclick_methods(self):
        """ondblclick shall round-trip via set/get with chaining and a None no-op."""
        map_obj = Map()
        value = String().setValue("dblclick()")

        result = map_obj.setOndblclick(value)
        assert result is map_obj
        assert map_obj.getOndblclick() is value

        map_obj.setOndblclick(None)
        assert map_obj.getOndblclick() is value

    MAP_PAGE_SPLIT_ATTRS = [
        ("setOnkeydown", "getOnkeydown", "keydown()"),
        ("setOnkeypress", "getOnkeypress", "keypress()"),
        ("setOnkeyup", "getOnkeyup", "keyup()"),
        ("setOnmousedown", "getOnmousedown", "mousedown()"),
        ("setOnmousemove", "getOnmousemove", "mousemove()"),
        ("setOnmouseout", "getOnmouseout", "mouseout()"),
        ("setOnmouseover", "getOnmouseover", "mouseover()"),
        ("setOnmouseup", "getOnmouseup", "mouseup()"),
        ("setTitle", "getTitle", "map title"),
    ]

    def test_map_page_split_attributes_get_set(self):
        """The page-split-fragment attributes shall round-trip with chaining and a None no-op."""
        for setter, getter, text in self.MAP_PAGE_SPLIT_ATTRS:
            map_obj = Map()
            result = getattr(map_obj, setter)(String().setValue(text))
            assert result is map_obj
            assert getattr(map_obj, getter)().getValue() == text
            getattr(map_obj, setter)(None)
            assert getattr(map_obj, getter)().getValue() == text


class TestLGraphic:
    """Test class for LGraphic class (AUTOSAR_FO_TPS_GenericStructureTemplate, Table 9.25)."""

    def test_l_graphic_base_chain(self):
        """LGraphic derives from LanguageSpecific (spec Base: ARObject , LanguageSpecific)."""
        from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import LanguageSpecific

        assert issubclass(LGraphic, LanguageSpecific)
        assert issubclass(LGraphic, ARObject)

    def test_l_graphic_initialization(self):
        """Test that an LGraphic object can be initialized with default values."""
        l_graphic = LGraphic()
        assert l_graphic.l is None
        assert l_graphic.graphic is None
        assert l_graphic.map is None

    def test_l_graphic_l_methods(self):
        """Test the l getter and setter."""
        l_graphic = LGraphic()
        l_val = "en"

        result = l_graphic.setL(l_val)
        assert l_graphic.getL() == l_val
        assert result == l_graphic

    def test_l_graphic_graphic_methods(self):
        """Test the graphic getter and setter with chaining and None no-op."""
        l_graphic = LGraphic()
        graphic = Graphic()

        result = l_graphic.setGraphic(graphic)
        assert l_graphic.getGraphic() == graphic
        assert result == l_graphic

        # A None value is a no-op and does not overwrite an existing graphic
        l_graphic.setGraphic(None)
        assert l_graphic.getGraphic() == graphic

    def test_l_graphic_map_methods(self):
        """Test the map getter and setter with chaining and None no-op."""
        l_graphic = LGraphic()
        map_obj = Map()

        result = l_graphic.setMap(map_obj)
        assert l_graphic.getMap() == map_obj
        assert result == l_graphic

        # A None value is a no-op and does not overwrite an existing map
        l_graphic.setMap(None)
        assert l_graphic.getMap() == map_obj

    def test_l_graphic_docstrings_verbatim(self):
        """Class and accessor docstrings must be the spec Note verbatim (Table 9.25)."""
        class_note = "This meta-class represents the figure in one particular language."
        graphic_note = "Reference to the actual graphic represented in the figure. Tags: xml.sequenceOffset=20"
        map_note = "Image maps enable authors to specify regions of an image or object and assign a specific action to each region. Tags: xml.sequenceOffset=30"

        assert inspect.cleandoc(LGraphic.__doc__) == class_note
        assert inspect.cleandoc(LGraphic.getGraphic.__doc__) == graphic_note
        assert inspect.cleandoc(LGraphic.getMap.__doc__) == map_note
        assert inspect.cleandoc(LGraphic.setGraphic.__doc__).startswith(graphic_note + ". A None value is a no-op")
        assert inspect.cleandoc(LGraphic.setMap.__doc__).startswith(map_note + ". A None value is a no-op")


class TestMlFigure:
    """Test class for MlFigure class."""

    def test_ml_figure_initialization(self):
        """Test that an MlFigure object can be initialized with default values."""
        ml_figure = MlFigure()
        assert ml_figure.figureCaption is None
        assert ml_figure.helpEntry is None
        assert ml_figure.lGraphics == []
        assert ml_figure.pgwide is None
        assert ml_figure.verbatim is None

    def test_ml_figure_figure_caption_methods(self):
        """Test the figureCaption getter and setter."""
        ml_figure = MlFigure()
        caption = "Test Caption"

        result = ml_figure.setFigureCaption(caption)
        assert ml_figure.getFigureCaption() == caption
        assert result == ml_figure

    def test_ml_figure_help_entry_methods(self):
        """Test the helpEntry getter and setter."""
        ml_figure = MlFigure()
        help_entry = String()

        result = ml_figure.setHelpEntry(help_entry)
        assert ml_figure.getHelpEntry() == help_entry
        assert result == ml_figure

    def test_ml_figure_l_graphics_methods(self):
        """Test adding language-specific graphics."""
        ml_figure = MlFigure()
        l_graphic = LGraphic()

        result = ml_figure.addLGraphics(l_graphic)
        l_graphics = ml_figure.getLGraphics()
        assert l_graphic in l_graphics
        assert result == ml_figure

    def test_ml_figure_pgwide_methods(self):
        """Test the pgwide getter and setter."""
        ml_figure = MlFigure()
        pgwide = "wide"

        result = ml_figure.setPgwide(pgwide)
        assert ml_figure.getPgwide() == pgwide
        assert result == ml_figure

    def test_ml_figure_verbatim_methods(self):
        """Test the verbatim getter and setter."""
        ml_figure = MlFigure()
        verbatim = "verbatim_text"

        result = ml_figure.setVerbatim(verbatim)
        assert ml_figure.getVerbatim() == verbatim
        assert result == ml_figure


class TestAreaEnumNohref:
    """Test class for AreaEnumNohref (AUTOSAR_FO_TPS_GenericStructureTemplate, Table 9.18)."""

    def test_area_enum_nohref_initialization(self):
        """Test that an AreaEnumNohref object can be initialized."""
        area_enum_nohref = AreaEnumNohref()
        assert area_enum_nohref is not None
        assert isinstance(area_enum_nohref, AreaEnumNohref)

    def test_area_enum_nohref_spec_literals(self):
        """AreaEnumNohref shall expose the 1 spec literal with its XSD string value."""
        enum = AreaEnumNohref()
        expected = {
            AreaEnumNohref.NOHREF: "NOHREF",
        }
        for const, value in expected.items():
            assert const == value
        assert set(enum.getEnumValues()) == set(expected.values())

    def test_area_enum_nohref_set_get_value(self):
        """setValue/getValue shall round-trip a spec literal."""
        enum = AreaEnumNohref().setValue(AreaEnumNohref.NOHREF)
        assert enum.getValue() == "NOHREF"

    def test_area_enum_nohref_validate_enum_value(self):
        """An invalid literal shall be rejected by validateEnumValue."""
        enum = AreaEnumNohref()
        assert enum.validateEnumValue("NOHREF") is True
        assert enum.validateEnumValue("HREF") is False


class TestAreaEnumShape:
    """Test class for AreaEnumShape (AUTOSAR_FO_TPS_GenericStructureTemplate, Table 9.19)."""

    def test_area_enum_shape_initialization(self):
        """Test that an AreaEnumShape object can be initialized."""
        area_enum_shape = AreaEnumShape()
        assert area_enum_shape is not None
        assert isinstance(area_enum_shape, AreaEnumShape)

    def test_area_enum_shape_spec_literals(self):
        """AreaEnumShape shall expose the 4 spec literals with their XSD string values."""
        enum = AreaEnumShape()
        expected = {
            AreaEnumShape.CIRCLE: "CIRCLE",
            AreaEnumShape.DEFAULT: "DEFAULT",
            AreaEnumShape.POLY: "POLY",
            AreaEnumShape.RECT: "RECT",
        }
        for const, value in expected.items():
            assert const == value
        assert set(enum.getEnumValues()) == set(expected.values())

    def test_area_enum_shape_set_get_value(self):
        """setValue/getValue shall round-trip a spec literal."""
        enum = AreaEnumShape().setValue(AreaEnumShape.RECT)
        assert enum.getValue() == "RECT"

    def test_area_enum_shape_validate_enum_value(self):
        """An invalid literal shall be rejected by validateEnumValue."""
        enum = AreaEnumShape()
        assert enum.validateEnumValue("RECT") is True
        assert enum.validateEnumValue("SQUARE") is False


class TestArea:
    """Test class for Area (AUTOSAR_FO_TPS_GenericStructureTemplate, Table 9.17)."""

    AREA_STRING_ATTRS = [
        ("accesskey", "setAccesskey", "getAccesskey"),
        ("alt", "setAlt", "getAlt"),
        ("class", "setClass", "getClass"),
        ("coords", "setCoords", "getCoords"),
        ("href", "setHref", "getHref"),
        ("onblur", "setOnblur", "getOnblur"),
        ("onclick", "setOnclick", "getOnclick"),
        ("ondblclick", "setOndblclick", "getOndblclick"),
        ("onfocus", "setOnfocus", "getOnfocus"),
        ("onkeydown", "setOnkeydown", "getOnkeydown"),
        ("onkeypress", "setOnkeypress", "getOnkeypress"),
        ("onkeyup", "setOnkeyup", "getOnkeyup"),
        ("onmousedown", "setOnmousedown", "getOnmousedown"),
        ("onmousemove", "setOnmousemove", "getOnmousemove"),
        ("onmouseout", "setOnmouseout", "getOnmouseout"),
        ("onmouseover", "setOnmouseover", "getOnmouseover"),
        ("onmouseup", "setOnmouseup", "getOnmouseup"),
        ("style", "setStyle", "getStyle"),
        ("tabindex", "setTabindex", "getTabindex"),
        ("title", "setTitle", "getTitle"),
    ]

    def test_area_initialization(self):
        """A new Area shall have all 22 spec attributes unset."""
        area = Area()
        assert area is not None
        assert isinstance(area, Area)
        for _, _, getter in self.AREA_STRING_ATTRS:
            assert getattr(area, getter)() is None
        assert area.getNohref() is None
        assert area.getShape() is None

    def test_area_string_attributes_get_set(self):
        """Each String attribute shall round-trip via set/get with chaining and a None no-op."""
        for _, setter, getter in self.AREA_STRING_ATTRS:
            area = Area()
            result = getattr(area, setter)(String().setValue("value"))
            assert result is area
            assert getattr(area, getter)().getValue() == "value"
            getattr(area, setter)(None)
            assert getattr(area, getter)().getValue() == "value"

    def test_area_nohref_get_set(self):
        """nohref shall accept an AreaEnumNohref value with chaining and a None no-op."""
        area = Area().setNohref(AreaEnumNohref().setValue(AreaEnumNohref.NOHREF))
        assert area.getNohref() is not None
        assert area.getNohref().getValue() == "NOHREF"
        area.setNohref(None)
        assert area.getNohref().getValue() == "NOHREF"

    def test_area_shape_get_set(self):
        """shape shall accept an AreaEnumShape value with chaining and a None no-op."""
        area = Area().setShape(AreaEnumShape().setValue(AreaEnumShape.RECT))
        assert area.getShape() is not None
        assert area.getShape().getValue() == "RECT"
        area.setShape(None)
        assert area.getShape().getValue() == "RECT"
