# Stage 1 — Docker builds this first, keeps it in memory as "builder"
FROM node:18-alpine AS builder
WORKDIR /app
COPY package*.json .
RUN npm install
COPY . .
RUN npm run build         
# Stage 2 — Docker builds this second
FROM nginx:alpine
COPY --from=builder /app/build /usr/share/nginx/html