"""
This module contains tests for the Figure module in MSR.Documentation.BlockElements.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import NameToken, String
from armodel.models.M2.MSR.Documentation.BlockElements.Figure import (
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
    """Test class for Map class."""

    def test_map_initialization(self):
        """Test that a Map object can be initialized."""
        map_obj = Map()
        assert map_obj is not None


class TestLGraphic:
    """Test class for LGraphic class."""

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
        """Test the graphic getter and setter."""
        l_graphic = LGraphic()
        graphic = Graphic()

        result = l_graphic.setGraphic(graphic)
        assert l_graphic.getGraphic() == graphic
        assert result == l_graphic

    def test_l_graphic_map_methods(self):
        """Test the map getter and setter."""
        l_graphic = LGraphic()
        map_obj = Map()

        result = l_graphic.setMap(map_obj)
        assert l_graphic.getMap() == map_obj
        assert result == l_graphic


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
