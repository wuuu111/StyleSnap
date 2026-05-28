import { useEffect, useState } from "react";

import { LookNavigation } from "./LookNavigation";
import { OutfitResultCard } from "./OutfitResultCard";
import type { RecommendedOutfit } from "../../types/outfit";

type OutfitCarouselProps = {
  candidateCount: number;
  occasion: string;
  outfits: RecommendedOutfit[];
  scoringVersion: string;
  targetStyle: string;
};

export function OutfitCarousel({
  candidateCount,
  occasion,
  outfits,
  scoringVersion,
  targetStyle,
}: OutfitCarouselProps) {
  const [currentIndex, setCurrentIndex] = useState(0);

  useEffect(() => {
    setCurrentIndex(0);
  }, [outfits]);

  const currentOutfit = outfits[currentIndex];

  if (!currentOutfit) {
    return null;
  }

  return (
    <div className="space-y-4">
      <div className="rounded-[24px] bg-mist p-4 text-sm text-ink/75">
        Candidates: {candidateCount} · Returned: {outfits.length} · {scoringVersion}
      </div>

      <LookNavigation
        currentIndex={currentIndex}
        onNext={() => setCurrentIndex((index) => Math.min(index + 1, outfits.length - 1))}
        onPrevious={() => setCurrentIndex((index) => Math.max(index - 1, 0))}
        total={outfits.length}
      />

      <OutfitResultCard
        lookIndex={currentIndex}
        occasion={occasion}
        outfit={currentOutfit}
        targetStyle={targetStyle}
        totalLooks={outfits.length}
      />
    </div>
  );
}
