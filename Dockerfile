## Nginx which can be run as any user (non-root docker user)
FROM nginx:1.21-alpine
RUN apk add --no-cache xxd python3
WORKDIR /home/project
RUN chown -R nginx:root /home/project

COPY nginx/nginx.conf /etc/nginx/
COPY nginx/default.conf /etc/nginx/conf.d/default.conf

USER nginx

COPY --chown=nginx:root nginx/index.html index.html
RUN chmod o=rw index.html
COPY --chown=nginx:root list.js .
COPY --chown=nginx:root nginx/start.py .
RUN chmod -R g=u /home/project

EXPOSE 8080
CMD ["python3", "start.py"]