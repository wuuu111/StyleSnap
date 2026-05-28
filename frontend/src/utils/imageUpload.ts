export const MAX_IMAGE_FILE_SIZE = 5 * 1024 * 1024;
export const IMAGE_UPLOAD_ERROR = "请上传图片文件，且大小不超过 5MB。";

export function validateImageFile(file: File) {
  if (!file.type.startsWith("image/")) {
    return IMAGE_UPLOAD_ERROR;
  }

  if (file.size > MAX_IMAGE_FILE_SIZE) {
    return IMAGE_UPLOAD_ERROR;
  }

  return null;
}

export function buildAnalyzeImageUrl(file: File, previewUrl: string) {
  const normalizedName = file.name.trim().toLowerCase();
  return normalizedName || previewUrl;
}

export function deriveItemNameFromFile(file: File) {
  const withoutExtension = file.name.replace(/\.[^/.]+$/, "");
  return withoutExtension.replace(/[-_]+/g, " ").trim();
}
