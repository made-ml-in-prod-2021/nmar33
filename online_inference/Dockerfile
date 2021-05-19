FROM python
COPY . .
RUN pip install -r requirements.txt

ENV CONFIG_PATH='./configs/config_lr.yaml'

CMD ["python", "start.py"]