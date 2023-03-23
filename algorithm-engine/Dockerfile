FROM harbor.flydiysz.cn:8888/flydiy-base/python38-base-algorithm-engine:v202303141306
ENV context_path /engine
COPY target/ /flydiy/${context_path}/
WORKDIR /flydiy/${context_path}
RUN ls -l
RUN cat requirements.txt
RUN awk 'BEGIN { cmd="cp -i ./conf/env.example.py   ./conf/env.py "; print "n" |cmd; }'
RUN python3 -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple/ -r requirements.txt
CMD ["./docker_start.sh"]
