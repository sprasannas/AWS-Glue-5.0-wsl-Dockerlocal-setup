FROM public.ecr.aws/glue/aws-glue-libs:5

WORKDIR /home/hadoop/workspace

COPY sample.py .
COPY config/job_params.json ./config/job_params.json
COPY requirements.txt .
RUN pip install -r requirements.txt


CMD ["spark-submit", "/home/hadoop/workspace/sample.py"]
