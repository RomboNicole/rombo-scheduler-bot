import datetime

class ScheduleBot:
    def __init__(self):
        self.schedule = []

    def add_event(self, event, date):
        try:
            date_obj = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M")
            self.schedule.append({"event": event, "date": date_obj})
            return f"✅ Event '{event}' added for {date_obj.strftime('%d %b %Y, %H:%M')}"
        except ValueError:
            return "⚠️ Invalid date format. Use YYYY-MM-DD HH:MM"

    def view_schedule(self):
        if not self.schedule:
            return "📭 No events scheduled."
        sorted_events = sorted(self.schedule, key=lambda x: x['date'])
        response = "📅 Your Schedule:\n"
        for item in sorted_events:
            response += f"- {item['event']} at {item['date'].strftime('%d %b %Y, %H:%M')}\n"
        return response

    def delete_event(self, event):
        for i, item in enumerate(self.schedule):
            if item['event'].lower() == event.lower():
                del self.schedule[i]
                return f"🗑️ Deleted event '{event}'"
        return f"❌ Event '{event}' not found."
