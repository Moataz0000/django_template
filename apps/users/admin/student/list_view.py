class StudentListView:
    list_display =  ("display_header", 'full_name', 'phone_number', 'class_number')
    list_editable = ()
    list_filter = ()
    date_hierarchy = None
    list_per_page = 20
    list_filter_submit = False
    list_fullwidth = False
    list_horizontal_scrollbar_top = False
    search_fields = ['phone_number']
    search_help_text = "Search by phone number..."

    def get_ordering(self, request):
        return ()
