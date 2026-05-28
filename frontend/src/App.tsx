import { Navigate, Route, Routes } from "react-router-dom";

import { AppShell } from "./components/AppShell";
import { AddItemPage } from "./pages/AddItemPage";
import { EditItemPage } from "./pages/EditItemPage";
import { LandingPage } from "./pages/LandingPage";
import { RecommendationPage } from "./pages/RecommendationPage";
import { WardrobePage } from "./pages/WardrobePage";

export default function App() {
  return (
    <Routes>
      <Route element={<AppShell />}>
        <Route index element={<LandingPage />} />
        <Route path="/wardrobe" element={<WardrobePage />} />
        <Route path="/wardrobe/new" element={<AddItemPage />} />
        <Route path="/wardrobe/:id/edit" element={<EditItemPage />} />
        <Route path="/recommendation" element={<RecommendationPage />} />
        <Route path="*" element={<Navigate to="/" replace />} />
      </Route>
    </Routes>
  );
}
