# Copyright 2025 University of Twente

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

# http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Use an official Python runtime as a parent image
FROM python:3.13.7-trixie

# Install packages
RUN apt-get update && apt-get -y install git
RUN pip3 install cairosvg

# Create folders
RUN mkdir /app
RUN mkdir /app/cpesdiag
RUN mkdir /app/cpesdiag/icons

# Copy files
WORKDIR /app

# Copy the sources that we require
COPY convertIcons.py /app/
COPY autoexec.sh /app/

# Create volume with output
VOLUME /app/cpesdiag/icons

# Setting the python path
ENV PYTHONPATH=/usr/lib/python3.13/site-packages
ENV PATH "$PATH:/app"

# Run autoexec.sh when the container launches
CMD sh /app/autoexec.sh