FROM public.ecr.aws/lambda/python:3.12

# Copy source code
COPY ./app/ ${LAMBDA_TASK_ROOT}/app/

# Copy requirements.txt
COPY ./requirements.txt ${LAMBDA_TASK_ROOT}

# Install dependencies
RUN pip install -r ${LAMBDA_TASK_ROOT}/requirements.txt

# !!! Adding code to python path
ENV PYTHONPATH="$PYTHONPATH:${LAMBDA_TASK_ROOT}"

# Set woring directory
WORKDIR ${LAMBDA_TASK_ROOT}/app

# Run the app
CMD ["main.handler"]