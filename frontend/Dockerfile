# Stage 1 - Builder
FROM node:18-slim AS builder

WORKDIR /app

COPY package*.json ./

RUN npm install

# Stage 2 - Final image
FROM node:18-slim

RUN useradd --create-home --shell /bin/bash appuser

WORKDIR /app

COPY --from=builder /app/node_modules ./node_modules

COPY app.js .
COPY views ./views
COPY package.json .

USER appuser

EXPOSE 3000

HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 CMD node -e "require('http').get('http://localhost:3000', (r) => r.statusCode === 200 ? process.exit(0) : process.exit(1)).on('error', () => process.exit(1))"

CMD ["node", "app.js"]
