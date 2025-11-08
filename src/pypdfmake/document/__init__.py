"""Document model exports for pypdfmake."""

from pypdfmake.document.definition import TDocumentDefinitions, AnyContent, ContentTypes
from pypdfmake.document.info import TDocumentInformation, PDFSubset, PDFVersion, Watermark
from pypdfmake.document.fonts import TFontFamilyTypes, TFontDictionary
from pypdfmake.document.patterns import Pattern, PatternDictionary, ImageDefinition, ImageDictionary

__all__ = [
    # Definition
    "TDocumentDefinitions",
    "AnyContent",
    "ContentTypes",
    # Info
    "TDocumentInformation",
    "PDFSubset",
    "PDFVersion",
    "Watermark",
    # Fonts
    "TFontFamilyTypes",
    "TFontDictionary",
    # Patterns
    "Pattern",
    "PatternDictionary",
    "ImageDefinition",
    "ImageDictionary",
]

# Rebuild document definition model to resolve forward references
TDocumentDefinitions.model_rebuild()
