from src.motivation.main import *
# from src.motivation.main import execute_ekoalt
from src.experiments.main import *

video_name = 'Dataset_Demo'
path = '/home/wwx/Videos'
images = load_dataset(video_name, path)

nb_buckets = int(len(images) * 0.1)
eko = execute_ekoalt(images, video_name, nb_buckets=nb_buckets)
query, times = query_process_aggregate(eko)

a = query.y_pred
b = query.y_true
gt_aggregate = []
for bb in b:
    gt_aggregate.append(float(bb))
gt_aggregate = np.array(gt_aggregate)
