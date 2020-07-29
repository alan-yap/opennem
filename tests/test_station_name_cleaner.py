from opennem.core.normalizers import station_name_cleaner


class TestStationNameCleaner(object):
    def test_stripping_units(self):
        name = "Eastern Creek LFG PS Units 1-4"
        subj = station_name_cleaner(name)

        assert subj == "Eastern Creek", "Eastern Creek should strip units"

    def test_power_stripper(self):
        name = "Test Power Station"
        subj = station_name_cleaner(name)

        assert subj == "Test", "Test power station becomes just Test"

    def test_acronyms(self):
        name = "agl power"
        subj = station_name_cleaner(name)

        assert subj == "AGL", "Acronym is AGL"

    def test_hallett_power(self):
        name = "Hallett Power Station"
        subj = station_name_cleaner(name)

        assert subj == "Hallett", "Hallet Power Station is Hallet"

    def test_hallet_is_three_units(self):
        hallet_names = [
            "Hallett Power Station",
            "Hallett 1 Wind Farm",
            "Hallett 2 Wind Farm",
        ]
        hallet_names_cleaned = list(
            set([station_name_cleaner(i) for i in hallet_names])
        )

        assert len(hallet_names) == len(
            hallet_names_cleaned
        ), "Hallet should have three distinct names"

    def test_grosvenor_stripping(self):
        name = "Grosvenor 1 Waste Coal Mine Gas Power Station"
        subject = station_name_cleaner(name)

        assert subject == "Grosvenor 1", "Grosvenor strips specifications"

    def test_unit_letters(self):
        name = "Yallourn 'W' Power Station"
        subject = station_name_cleaner(name)

        assert subject == "Yallourn W", "Yallourn has a unit letter"

    # Slash names

    def test_dashed_names(self):
        name = "Catagunya / Liapootah / Wayatinah"
        subject = station_name_cleaner(name)

        assert (
            subject == "Catagunya / Liapootah / Wayatinah"
        ), "Catagunya slash name"

    def test_dashed_names_whitespace(self):
        name = "Catagunya/Liapootah / Wayatinah"
        subject = station_name_cleaner(name)

        assert (
            subject == "Catagunya / Liapootah / Wayatinah"
        ), "Catagunya slash name whitespaced correctly"

    def test_dashed_names_whitespace_capitalized(self):
        name = "catagunya/liapootah / wayatinah"
        subject = station_name_cleaner(name)

        assert (
            subject == "Catagunya / Liapootah / Wayatinah"
        ), "Catagunya slash name whitespaced and capitalized correctly"

    def test_dashed_names_with_stripping(self):
        name = "Catagunya / Liapootah / Wayatinah Power Station"
        subject = station_name_cleaner(name)

        assert (
            subject == "Catagunya / Liapootah / Wayatinah"
        ), "Catagunya hyphenated name"

    # Mappings

    def test_name_mapping_and_stripping(self):
        name = "SA Government Virtual Power Plant - stage 1"
        subject = station_name_cleaner(name)

        assert (
            subject == "SA VPP"
        ), "SA Government Virtual Power Plant maps to SA VPP"

    def test_name_mapping_hornsdale(self):
        name = "Hornsdale Power Reserve Unit 1"
        subject = station_name_cleaner(name)

        assert subject == "Hornsdale Power Reserve", "Hornsdale maps"
