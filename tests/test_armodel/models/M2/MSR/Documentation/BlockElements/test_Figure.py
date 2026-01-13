"""
This module contains tests for the Figure module in MSR.Documentation.BlockElements.
"""
import pytest
from armodel.models.M2.MSR.Documentation.BlockElements.Figure import *
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import LanguageSpecific
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum, String


class TestGraphicFitEnum:
    """Test class for GraphicFitEnum class."""
    
    def test_graphic_fit_enum_initialization(self):
        """Test that a GraphicFitEnum object can be initialized."""
        graphic_fit_enum = GraphicFitEnum([])
        assert graphic_fit_enum is not None


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
    
    def test_graphic_editfit_methods(self):
        """Test the editfit getter and setter."""
        graphic = Graphic()
        editfit = GraphicFitEnum([])
        
        result = graphic.setEditfit(editfit)
        assert graphic.getEditfit() == editfit
        assert result == graphic
    
    def test_graphic_edit_height_methods(self):
        """Test the editHeight getter and setter."""
        graphic = Graphic()
        height = String()
        
        result = graphic.setEditHeight(height)
        assert graphic.getEditHeight() == height
        assert result == graphic
    
    def test_graphic_editscale_methods(self):
        """Test the editscale getter and setter."""
        graphic = Graphic()
        scale = String()
        
        result = graphic.setEditscale(scale)
        assert graphic.getEditscale() == scale
        assert result == graphic
    
    def test_graphic_edit_width_methods(self):
        """Test the editWidth getter and setter."""
        graphic = Graphic()
        width = String()
        
        result = graphic.setEditWidth(width)
        assert graphic.getEditWidth() == width
        assert result == graphic
    
    def test_graphic_filename_methods(self):
        """Test the filename getter and setter."""
        graphic = Graphic()
        filename = String()
        
        result = graphic.setFilename(filename)
        assert graphic.getFilename() == filename
        assert result == graphic
    
    def test_graphic_fit_methods(self):
        """Test the fit getter and setter."""
        graphic = Graphic()
        fit = GraphicFitEnum([])
        
        result = graphic.setFit(fit)
        assert graphic.getFit() == fit
        assert result == graphic


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