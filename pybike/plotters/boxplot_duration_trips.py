from datetime import datetime

import pandas as pd
import plotly.express as px


class BoxplotDurationPlotter:
    def __init__(self):
        pass

    def set_plotting_data(
        self,
        trips_df,
        start_date=datetime(2013, 9, 1),
        end_date=datetime(2014, 9, 1),
        stations_names=None,
        duration_min=None,
        duration_max=None,
    ):
        # Filter by start_date and end_date
        filtered_trips_df = trips_df[
            (trips_df["start_date"] >= start_date)
            & (trips_df["start_date"] <= end_date)
        ].copy()

        # Filter by stations_names if provided
        if stations_names:
            filtered_trips_df = filtered_trips_df[
                filtered_trips_df["start_station_name"].isin(stations_names)
            ]

        # Filter by duration_min if provided
        if duration_min is not None:
            filtered_trips_df = filtered_trips_df[
                filtered_trips_df["duration"] >= duration_min
            ]

        # Filter by duration_max if provided
        if duration_max is not None:
            filtered_trips_df = filtered_trips_df[
                filtered_trips_df["duration"] <= duration_max
            ]

        return filtered_trips_df

    def set_plotting_data_per_station_day(
        self,
        trips_df,
        start_date=datetime(2013, 9, 1),
        end_date=datetime(2014, 9, 1),
        stations_names=None,
        duration_min=None,
        duration_max=None,
    ):
        # Filtrar los datos básicos
        filtered_trips_df = self.set_plotting_data(
            trips_df,
            start_date,
            end_date,
            stations_names,
            duration_min,
            duration_max,
        )

        # Extraer el nombre del día de la semana
        filtered_trips_df["day_name"] = filtered_trips_df["start_date"].dt.day_name()

        # Ordenar los días de la semana
        days_of_week = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ]
        filtered_trips_df["day_name"] = pd.Categorical(
            filtered_trips_df["day_name"], categories=days_of_week, ordered=True
        )

        return filtered_trips_df

    def plot(
        self,
        trips_df,
        start_date=datetime(2013, 9, 1),
        end_date=datetime(2013, 10, 1),
        stations_names=None,
        combine_stations=True,
        duration_min=None,
        duration_max=None,
    ):
        # Get the filtered data
        filtered_trips_df = self.set_plotting_data(
            trips_df,
            start_date,
            end_date,
            stations_names,
            duration_min,
            duration_max,
        )

        if combine_stations:
            fig = px.box(filtered_trips_df, y="duration", title="Trip Duration Boxplot")
            fig.update_layout(yaxis_title="Duration")
        else:
            fig = px.box(
                filtered_trips_df,
                x="start_station_name",
                y="duration",
                title="Trip Duration Boxplot by Station",
            )
            fig.update_layout(xaxis_title="Start Station", yaxis_title="Duration")

        return fig

    def plot_per_station_day(
        self,
        trips_df,
        start_date=datetime(2013, 9, 1),
        end_date=datetime(2013, 10, 1),
        stations_names=None,
        duration_min=None,
        duration_max=None,
    ):
        # Obtener los datos filtrados con información del día de la semana
        filtered_trips_df = self.set_plotting_data_per_station_day(
            trips_df,
            start_date,
            end_date,
            stations_names,
            duration_min,
            duration_max,
        )

        # Crear el boxplot
        fig = px.box(
            filtered_trips_df,
            x="start_station_name",
            y="duration",
            color="day_name",
            title="Trip Duration Boxplot by Station and Day of Week",
            category_orders={
                "day_name": [
                    "Monday",
                    "Tuesday",
                    "Wednesday",
                    "Thursday",
                    "Friday",
                    "Saturday",
                    "Sunday",
                ]
            },
        )

        fig.update_layout(
            xaxis_title="Start Station",
            yaxis_title="Duration",
            legend_title="Day of Week",
        )

        return fig