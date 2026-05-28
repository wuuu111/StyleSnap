from __future__ import annotations


class VisionProviderPlaceholder:
    def analyze_clothing_image(self, *, image_reference: str) -> dict:
        raise NotImplementedError("Real vision provider is not configured yet.")
