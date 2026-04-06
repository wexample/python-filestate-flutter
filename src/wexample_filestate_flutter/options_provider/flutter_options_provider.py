from __future__ import annotations

from typing import TYPE_CHECKING

from wexample_config.options_provider.abstract_options_provider import (
    AbstractOptionsProvider,
)

if TYPE_CHECKING:
    from wexample_config.config_option.abstract_config_option import (
        AbstractConfigOption,
    )


class FlutterOptionsProvider(AbstractOptionsProvider):
    @classmethod
    def get_docker_image_name(cls) -> str | None:
        from wexample_filestate_flutter.option.flutter.abstract_flutter_file_content_option import (
            AbstractFlutterFileContentOption,
        )

        return AbstractFlutterFileContentOption.DOCKER_IMAGE_NAME

    @classmethod
    def get_options(cls) -> list[type[AbstractConfigOption]]:
        from wexample_filestate_flutter.option.flutter_option import FlutterOption

        return [
            FlutterOption,
        ]
