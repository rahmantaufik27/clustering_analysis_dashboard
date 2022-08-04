from flask import Flask, send_file, render_template, Response
import io
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib.pyplot as plt 
import seaborn as sns
from models.clustering import visualize

app = Flask(__name__)

# initialization
v = visualize()

@app.route("/")
def home():
    statistic_value = {}
    student, test, session = v.info_statistic()
    statistic_value["student"] = student
    statistic_value["test"] = test
    statistic_value["session"] = session
    # print(statistic_value)
    return render_template("post_uts.html", statistic_value=statistic_value)

@app.route("/info_statistic")
def info_statistic():
    statistic_value = {}
    student, test, session = v.info_statistic()
    statistic_value["student"] = student
    statistic_value["test"] = test
    statistic_value["session"] = session
    # print(statistic_value)
    return render_template("post_uts.html", statistic_value=statistic_value)

# @app.route("/scatter")
# def scatter():
#     # load the data
#     x_scaled, df_clustering = v.cluster_scatter_plot()
#     # set the plot
#     fig_sct, ax = plt.subplots(figsize=(6,4))
#     sns.scatterplot(x_scaled[:,0], x_scaled[:,1], hue=df_clustering["kluster"], palette="deep", alpha=0.8, s=50)
#     canvas_sct = FigureCanvas(fig_sct)
#     img_sct = io.BytesIO()
#     fig_sct.savefig(img_sct)
#     img_sct.seek(0)
#     # send for display
#     return send_file(img_sct, mimetype="img/png")

# @app.route("/bar")
# def bar():
#     df1, df2, df3 = v.cluster_distribution_bar_plot()
#     df1 = df1[["score_y"]]
#     # print(df1)
#     # print(df1.isnull().any())
#     fig_bar, ax = plt.subplots(figsize=(6,4))
#     # sns.scatterplot(df1["score_x"], df1["score_y"], palette="deep", alpha=0.8, s=50)
#     sns.displot(df1)
#     # x = ['A', 'B', 'C']
#     # y = [1, 5, 3]

#     # sns.barplot(df1)
#     canvas_bar = FigureCanvas(fig_bar)
#     img_bar = io.BytesIO()
#     fig_bar.savefig(img_bar)
#     img_bar.seek(0)
#     # plt.savefig('static/images/plot.png')
#     # return send_file(fig_bar, mimetype="img/png")
#     return render_template("post_uts.html", url_img_displot="/static/images/displot.png")

# call the main
if __name__ == "__main__":
    # app.run()
    app.run(debug=True, host="0.0.0.0", port=2700)