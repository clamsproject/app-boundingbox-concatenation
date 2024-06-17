# Use the same base image version as the clams-python python library version
FROM ghcr.io/clamsproject/clams-python:1.2.4
################################################################################
# DO NOT EDIT THIS SECTION
ARG CLAMS_APP_VERSION
ENV CLAMS_APP_VERSION ${CLAMS_APP_VERSION}
################################################################################

################################################################################
# This is duplicate from the base image Containerfile 
# but makes sure the cache directories are consistent across all CLAMS apps

# https://github.com/openai/whisper/blob/ba3f3cd54b0e5b8ce1ab3de13e32122d0d5f98ab/whisper/__init__.py#L130
ENV XDG_CACHE_HOME='/cache'  
# https://huggingface.co/docs/huggingface_hub/main/en/package_reference/environment_variables#hfhome
ENV HF_HOME="/cache/huggingface"
# https://pytorch.org/docs/stable/hub.html#where-are-my-downloaded-models-saved
ENV TORCH_HOME="/cache/torch"

# RUN mkdir /cache && rm -rf /root/.cache && ln -s /cache /root/.cache
################################################################################
# clams-python base images are based on debian distro
# install more system packages as needed using the apt manager
################################################################################

################################################################################
# main app installation
COPY ./ /app
WORKDIR /app
RUN pip3 install -r requirements.txt

# default command to run the CLAMS app in a production server 
CMD ["python3", "app.py", "--production"]
################################################################################
