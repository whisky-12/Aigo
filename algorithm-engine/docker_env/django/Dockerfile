FROM xzj746753491/python38-base-algorithm-engine:latest
WORKDIR /
COPY ./ .
RUN awk 'BEGIN { cmd="cp -i ./conf/env.example.py   ./conf/env.py "; print "n" |cmd; }'
RUN python3 -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple/ -r requirements.txt
CMD ["/docker_start.sh"]
