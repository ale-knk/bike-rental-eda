from datetime import datetime

import pandas as pd
import plotly.express as px


class HeatMapTripsPlotter:
    def __init__(self):
        pass

    def set_layout(self, fig, plot_df):
        # Opcional: Puedes personalizar el layout según tus necesidades
        fig.update_layout(
            title={
                "text": "Heatmap de Viajes entre Estaciones",
                "font": {"size": 24},
                "x": 0.5,
                "xanchor": "center",
            },
            xaxis_title="Estación de Origen",
            yaxis_title="Estación de Destino",
            dragmode="zoom",
        )

        fig.update_xaxes(tickfont=dict(size=10))
        fig.update_yaxes(tickfont=dict(size=10))

    def set_plotting_data(
        self,
        trips_df,
        start_date=datetime(2013, 9, 1),
        end_date=datetime(2013, 10, 1),
        stations=None,
    ):
        # Filtrar por fechas
        filtered_trips_df = trips_df[
            (trips_df["start_date"] >= start_date)
            & (trips_df["start_date"] <= end_date)
        ]

        # Filtrar por estaciones si se proporcionan
        if stations:
            filtered_trips_df = filtered_trips_df[
                filtered_trips_df["start_station_name"].isin(stations)
                & filtered_trips_df["end_station_name"].isin(stations)
            ]

        # Agrupar por estación de origen y destino y contar los viajes
        trips_heatmap = (
            filtered_trips_df.groupby(["start_station_name", "end_station_name"])
            .size()
            .reset_index(name="count")
        )

        # Crear una tabla pivote para el heatmap
        heatmap_pivot = trips_heatmap.pivot(
            index="end_station_name", columns="start_station_name", values="count"
        ).fillna(0)

        return heatmap_pivot

    def plot(
        self,
        trips_df,
        start_date=datetime(2013, 9, 1),
        end_date=datetime(2013, 10, 1),
        stations=None,
    ):
        plot_df = self.set_plotting_data(trips_df, start_date, end_date, stations)

        # Crear el heatmap usando Plotly Express
        fig = px.imshow(
            plot_df,
            labels=dict(
                x="Estación de Origen",
                y="Estación de Destino",
                color="Número de Viajes",
            ),
            x=plot_df.columns,
            y=plot_df.index,
            color_continuous_scale="Viridis",
            title="Número de Viajes entre Estaciones",
            aspect="auto"
        )

        # Personalizar el layout
        self.set_layout(fig, plot_df)

        return fig
