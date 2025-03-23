FROM node:23-alpine

WORKDIR /app

# Install dependencies
COPY package.json package-lock.json ./
RUN npm ci

# Copy project files
COPY . .

# Expose port
EXPOSE 4200

# Start development server with host set to 0.0.0.0 to allow external access
CMD ["npm", "start", "--", "--host", "0.0.0.0"]
