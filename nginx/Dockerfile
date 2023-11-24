# Используем официальный образ Nginx в качестве базового образа
FROM nginx:latest

# Удаляем стандартный конфигурационный файл Nginx
RUN rm /etc/nginx/conf.d/default.conf

# Копируем нашу кастомную конфигурацию Nginx
COPY nginx/nginx.conf /etc/nginx/conf.d/

# Копируем статические файлы в соответствующую директорию
COPY nginx/static /usr/share/nginx/html/static
