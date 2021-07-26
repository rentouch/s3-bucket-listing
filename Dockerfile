## Nginx which can be run as any user (non-root docker user)
FROM nginx:1.21-alpine
RUN apk add --no-cache xxd python3
WORKDIR /home/project

COPY nginx/nginx.conf /etc/nginx/
COPY nginx/default.conf /etc/nginx/conf.d/default.conf

USER nginx
COPY --chown=nginx:root nginx/index.html index.html
COPY list.js .
COPY nginx/start.py .

EXPOSE 8080
CMD ["python3", "start.py"]