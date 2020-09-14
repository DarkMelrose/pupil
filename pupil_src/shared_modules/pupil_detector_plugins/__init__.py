"""
(*)~---------------------------------------------------------------------------
Pupil - eye tracking platform
Copyright (C) 2012-2020 Pupil Labs

Distributed under the terms of the GNU
Lesser General Public License (LGPL v3.0).
See COPYING and COPYING.LESSER for license details.
---------------------------------------------------------------------------~(*)
"""
import logging
import typing as T

from .detector_2d_plugin import Detector2DPlugin
from .detector_base_plugin import PupilDetectorPlugin, EVENT_KEY

logger = logging.getLogger(__name__)


def available_detector_plugins() -> T.Tuple[
    T.Optional[PupilDetectorPlugin],
    T.Optional[PupilDetectorPlugin],
    T.List[PupilDetectorPlugin],
]:
    """Load and list available plugins, including default

    Returns tuple of default2D, default3D, and list of all detectors.
    """

    all_plugins = [Detector2DPlugin]
    default2D = Detector2DPlugin
    default3D = None

    try:
        from .pye3d_plugin import Pye3DPlugin
    except ImportError:
        logger.info("Refraction corrected 3D pupil detector not available!")
    else:
        logger.info("Using refraction corrected 3D pupil detector.")
        all_plugins.append(Pye3DPlugin)
        default3D = Pye3DPlugin

    if default3D is None:
        logger.warning("No 3D pupil detector is available!")

    return default2D, default3D, all_plugins
