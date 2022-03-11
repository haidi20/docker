FROM python:3.8-alpine

# The latest alpine images don't have some tools like (`git` and `bash`).
# Adding git, bash and openssh to the image
# RUN apk update && apk upgrade && \ 
#     apk add --no-cache git

# Make dir app
RUN mkdir -p /app
WORKDIR /app

# add file index.py
ADD index.py /app

# Run the executable
CMD ["python", "./index.py"]

