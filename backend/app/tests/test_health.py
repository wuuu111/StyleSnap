def test_health_endpoint_reports_service_status(client) -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "service": "stylesnap-backend",
        "database": "sqlite",
    }
