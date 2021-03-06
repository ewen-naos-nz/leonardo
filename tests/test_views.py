import unittest
import leonardo
from mock import Mock


class ViewsTest(unittest.TestCase):

    def setUp(self):
        '''
        creates a fake category and points it to a dashboard in the tests directory.
        '''
        l = leonardo.leonardo.Leonardo()
        c = leonardo.category.Category
        d_options = {'graph_columns': 2}
        d = leonardo.dashboard.Dashboard('server-1', 'tests/data/graphs', 'System', d_options )
        c.dashboard = Mock()
        c.dashboard.return_value = d
        c.dashboards = Mock()
        c.dashboards.return_value = [d]
        l.top_level['System'] = c
        l.top_level['System'].dashboard = Mock()
        l.top_level['System'].dashboard.return_value = d

        self.app = leonardo.app.test_client()


    def _test_url(self, url):
        rv = self.app.get(url)
        assert rv.status == '200 OK'

    def test_root_route_status(self):
        self._test_url('/')

    def test_dash_route_status(self):
        self._test_url('/System/server-1/')

    def test_details_route_status(self):
        self._test_url('/System/server-1/details/cpu/')

    def test_single_route_status(self):
        self._test_url('/System/server-1/single/cpu/')

    def test_full_view_status(self):
        self._test_url('/System/server-1/?full=yes')

    def test_api_dash_route_status(self):
        self._test_url('/api/System/server-1/')

    def test_api_details_route_status(self):
        self._test_url('/api/System/server-1/single/cpu/')
