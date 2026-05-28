export type ApiErrorResponse = {
  error: {
    code: string;
    message: string;
    details: Record<string, unknown>;
  };
};

export class ApiError extends Error {
  code: string;
  details: Record<string, unknown>;

  constructor(payload: ApiErrorResponse["error"]) {
    super(payload.message);
    this.name = "ApiError";
    this.code = payload.code;
    this.details = payload.details;
  }
}
