import plotly.express as px

def create_bar_chart(df, x_col, y_col, title):
    fig = px.bar(df, x=x_col, y=y_col, title=title, template="plotly_white", color=y_col)
    fig.update_layout(margin=dict(l=20, r=20, t=40, b=20))
    return fig

def create_pie_chart(df, names_col, values_col, title):
    fig = px.pie(df, names=names_col, values=values_col, title=title, hole=0.4)
    fig.update_layout(margin=dict(l=20, r=20, t=40, b=20))
    return fig
