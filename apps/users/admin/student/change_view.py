class StudentChangeView:
    filter_horizontal = ()
    compressed_fields = True
    autocomplete_fields = ()
    fieldsets = (
        ("Student", {"fields": ('username', 'phone_number', 'full_name', 'class_number', 'image')}),
    )
