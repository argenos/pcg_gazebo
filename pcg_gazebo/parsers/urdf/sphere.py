# Copyright (c) 2019 - The Procedural Generation for Gazebo authors
# For information on the respective copyright owner see the NOTICE file
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import random
from ..types import XMLBase
from ...utils import is_scalar


class Sphere(XMLBase):
    _NAME = 'sphere'
    _TYPE = 'urdf'

    _ATTRIBUTES = dict(
        radius='0'
    )

    def __init__(self):
        XMLBase.__init__(self)
        self.reset()

    @property
    def radius(self):
        return float(self.attributes['radius'])

    @radius.setter
    def radius(self, value):
        assert is_scalar(value), 'Radius must be a positive scalar'
        self.attributes['radius'] = '{}'.format(value)

    def to_sdf(self):
        from ..sdf import create_sdf_element

        obj = create_sdf_element('sphere')
        obj.radius = self.radius
        return obj

    def random(self):
        self.radius = random.random()
