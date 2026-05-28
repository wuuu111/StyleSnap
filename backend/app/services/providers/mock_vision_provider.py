from __future__ import annotations

from app.schemas.clothing import ClothingAnalyzeResponse


class MockVisionProvider:
    def analyze_clothing_image(self, *, image_reference: str) -> ClothingAnalyzeResponse:
        normalized = image_reference.lower().strip()

        if not normalized:
            raise ValueError("Image URL is required")

        if any(keyword in normalized for keyword in ["white", "shirt", "tshirt", "tee"]):
            return ClothingAnalyzeResponse(
                name="White T-shirt",
                image_url=image_reference,
                category="top",
                color="white",
                style_tags=["Clean Fit", "casual"],
                season_tags=["summer"],
                thickness="thin",
                min_temperature=20,
                max_temperature=32,
                rain_suitable=False,
                occasion_tags=["上课", "休闲"],
                notes="Mock AI generated clothing metadata.",
            )

        if any(keyword in normalized for keyword in ["jeans", "denim"]):
            return ClothingAnalyzeResponse(
                name="Dark Jeans",
                image_url=image_reference,
                category="pants",
                color="navy",
                style_tags=["美式复古", "casual"],
                season_tags=["all-season"],
                thickness="medium",
                min_temperature=8,
                max_temperature=28,
                rain_suitable=True,
                occasion_tags=["休闲"],
                notes="Mock AI generated clothing metadata.",
            )

        if any(keyword in normalized for keyword in ["jacket", "coat"]):
            return ClothingAnalyzeResponse(
                name="Black Jacket",
                image_url=image_reference,
                category="outerwear",
                color="black",
                style_tags=["通勤", "简约"],
                season_tags=["autumn", "winter"],
                thickness="thick",
                min_temperature=5,
                max_temperature=18,
                rain_suitable=True,
                occasion_tags=["通勤"],
                notes="Mock AI generated clothing metadata.",
            )

        if any(keyword in normalized for keyword in ["sneaker", "shoe", "shoes"]):
            return ClothingAnalyzeResponse(
                name="White Sneakers",
                image_url=image_reference,
                category="shoes",
                color="white",
                style_tags=["Clean Fit", "运动休闲"],
                season_tags=["all-season"],
                thickness="medium",
                min_temperature=0,
                max_temperature=32,
                rain_suitable=False,
                occasion_tags=["上课", "通勤"],
                notes="Mock AI generated clothing metadata.",
            )

        if any(keyword in normalized for keyword in ["cap", "hat"]):
            return ClothingAnalyzeResponse(
                name="Baseball Cap",
                image_url=image_reference,
                category="hat",
                color="black",
                style_tags=["运动休闲", "美式复古"],
                season_tags=["summer"],
                thickness="thin",
                min_temperature=18,
                max_temperature=35,
                rain_suitable=False,
                occasion_tags=["休闲"],
                notes="Mock AI generated clothing metadata.",
            )

        return ClothingAnalyzeResponse(
            name="Unknown Item",
            image_url=image_reference,
            category="accessory",
            color="gray",
            style_tags=["casual"],
            season_tags=["all-season"],
            thickness="medium",
            min_temperature=10,
            max_temperature=26,
            rain_suitable=True,
            occasion_tags=["休闲"],
            notes="Mock AI generated fallback clothing metadata.",
        )
