"""
The purpose of this file is to define the metadata of the app with minimal imports. 

DO NOT CHANGE the name of the file
"""

from mmif import DocumentTypes, AnnotationTypes

from clams.app import ClamsApp
from clams.appmetadata import AppMetadata


# DO NOT CHANGE the function name
def appmetadata() -> AppMetadata:
    """
    Function to set app-metadata values and return it as an ``AppMetadata`` obj.
    Read these documentations before changing the code below
    - https://sdk.clams.ai/appmetadata.html metadata specification.
    - https://sdk.clams.ai/autodoc/clams.appmetadata.html python API

    :return: AppMetadata object holding all necessary information.
    """

    # ================================|
    # Metadata
    metadata = AppMetadata(
        name="BoundingBox Concatenation",
        description="Converts a series of bounding-boxes at a given timepoint into a single bounding box.",
        app_license="MIT",
        identifier="app-boundingbox-concatenation",
        url="https://github.com/clamsproject/app-boundingbox-concatenation",
    )

    # ================================|
    # IO Spec
    metadata.add_input(DocumentTypes.Document)
    metadata.add_input(AnnotationTypes.BoundingBox)
    metadata.add_input(AnnotationTypes.Alignment)
    metadata.add_output(AnnotationTypes.BoundingBox)

    # ================================|
    # Runtime Parameters
    metadata.add_parameter(
        name="timeUnit",
        description="the division of time processing",
        type="string",
        choices=["frames", "seconds", "milliseconds"],
        default="frames",
    )
    metadata.add_parameter(
        name="boxType",
        description="the type of boxes that are being concatenated",
        default="text",
        type="string",
    )
    return metadata


# DO NOT CHANGE the main block
if __name__ == "__main__":
    import sys

    metadata = appmetadata()
    for param in ClamsApp.universal_parameters:
        metadata.add_parameter(**param)
    sys.stdout.write(metadata.jsonify(pretty=True))
