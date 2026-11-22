FROM golang:1.24.4-alpine AS build

WORKDIR /app

COPY ./cmdb-37/app/. .

RUN go mod tidy && \
    CGO_ENABLED=0 GOOS=linux go build -trimpath -ldflags="-s -w" -o /bin/app-api .

FROM alpine
COPY --from=build /bin/app-api /app-api
CMD ["/app-api"]
